# -*- coding: utf-8 -*-

import odoo
from odoo import http
from odoo.http import request
import logging
import erppeek

DBNAME_PATTERN = '^[a-zA-Z0-9][a-zA-Z0-9_.-]+$'

_logger = logging.getLogger(__name__)

class TCMPlatformWizard(http.Controller):
    @http.route('/build_client/launch/wizard', type='http', auth="public", website=False, csrf=False)
    def launch_wizard(self, **kw):
        d = {}
        d['manage'] = True
        # d.setdefault('manage', True)
        d['insecure'] = odoo.tools.config.verify_admin_password('admin')
        d['list_db'] = odoo.tools.config['list_db']
        d['langs'] = odoo.service.db.exp_list_lang()
        d['countries'] = odoo.service.db.exp_list_countries()
        d['pattern'] = DBNAME_PATTERN
        # databases list
        d['databases'] = []
        # print('Diccionario d:', d)

        return request.render("tcm_build_client.build_client_wizard", d)
        # Finished!

    @http.route('/build_client/database/create', type='http', auth="public", website=True, csrf=False)
    def create_database(self, **post):

        # logger.debug("No moment locale for code %s", code)
        # logger.warning("No email template found for sending email to the portal user")

        print('Master password: ', post.get('master_pwd'))
        print('Name: ', post.get('name'))
        print('Email: ', post.get('login'))
        print('Password: ', post.get('password'))
        print('Phone: ', post.get('phone'))
        print('Idioma: ', post.get('lang'))
        print('Pais: ', post.get('country_code'))
        print('Datos Demos: ', post.get('demo'))
        print('Plan: ', post.get('product'))
        print('Metodo de Pago: ', post.get('paymethod'))

        # IP real del servidor Nginx
        # real_ip_address = request.httprequest.environ['HTTP_X_REAL_IP']
        real_ip_address = request.httprequest.environ.get('HTTP_X_REAL_IP')
        ip_server = None

        pool_config = request.env['ir.config_parameter'].search([('key', '=', 'web.base.url')])[0]
        ip_server = pool_config.value
        print('IP del servidor: ', ip_server)

        # if (real_ip_address == None):
        #     pool_config = request.env['ir.config_parameter'].search([('key', '=', 'web.base.url')])[0]
        #     ip_server = pool_config.value
        #     print('IP del servidor: ', ip_server)
        #     _logger.info('IP real del servidor: %s', ip_server)
        # else:
        #     ip_server = real_ip_address
        #     print('IP real del servidor: ', )
        #     _logger.info('IP real del servidor: %s', ip_server)

        ADMIN_PASSWORD = post.get('master_pwd')
        SERVER = ip_server
        # XSERVER = request.env["ir.config_parameter"].get_param("server")
        DATABASE = post.get('name')
        LOGIN = post.get('login')
        USER_PASSWORD = post.get('password')
        LANG = post.get('lang')
        COUNTRY_CODE = post.get('country_code')
        DEMO = False

        client = erppeek.Client(server=SERVER)
        status = {}
        try:
            if not DATABASE in client.db.list():
                # print("La base de datos no existe, creando una!")
                client.create_database(ADMIN_PASSWORD, DATABASE, DEMO, LANG, USER_PASSWORD, LOGIN, COUNTRY_CODE)
                status['message'] = 'Instancia de Odoo (' + DATABASE + ') se creó con éxito!!!'
                _logger.debug("La base de datos se ha creado con exito!")

                # Instalando los modulos necesarios
                self.install_odoo_modules(SERVER, DATABASE, LOGIN, USER_PASSWORD)
                print("Modulos instalados con exito!")
            else:
                # print("La base de datos " % DATABASE % " ya existe")
                status['message'] = "La base de datos (" + DATABASE + ") ya existe, por favor seleccione otro nombre."
                _logger.warning("La base de datos " + DATABASE + " ya existe")
        except Exception as e:
            error = "Database creation error: %s" % (str(e) or repr(e))
            status['message'] = error
            _logger.exception("Database creation error: %s" % (str(e) or repr(e)))
            # print(error)

        return request.render("tcm_build_client.build_client_wizard_report", status)
        # Finished!

    def install_odoo_modules(self, serverName, database, login, password):
        # You can use this client if you have Erppeek installed and have a erppeek.ini file
        # client = erppeek.Client.from_config('ErpPeekDemoDatabase')
        # The alternative is by specifying the settings by command
        # client = erppeek.Client('http://localhost:8080', 'ErpPeekDemoDatabase', 'admin', 'admin')
        client = erppeek.Client(serverName, database, login, password)
        print('Instalando los modulos...')
        modules = client.modules('tcm_client_access', installed=False)
        if 'tcm_client_access' in modules['uninstalled']:
            # client.install('tcm_client_access','hr','point_of_sale','website_sale')
            client.install('tcm_client_access')
            print('Los modulos seleccionados han sido instalado!')


    # If you want to install module on any button event from your custome module you can use below code:
    def install_odoo_modules_test1(self):
        pool = request.env['ir.module']
        module_obj = pool.get('ir.module.module')
        module_list = ['web','point_of_sale','tcm_client_access']
        module_ids_to_install = module_obj.search(cr, 1, [('name','in',module_list)])
        module_obj.update_list(cr, 1, context=None)  # just to update module list to update new module added
        module_obj.button_immediate_install(cr, 1, module_ids_to_install, context=context)

    def install_odoo_modules_test2(self):
        irModuleObj = request.env['ir.module.module']
        irModuleObj.update_list()
        moduleIds = irModuleObj.search(
            [
                ('state', '!=', 'installed'),
                ('name', '=', 'technical name of module')
            ]
        )
        if moduleIds:
            moduleIds[0].button_immediate_install()

    @http.route('/build_client/database/test_install', type='http', auth="public", website=True, csrf=False)
    def wizard_example(self, **d):
        SERVER = 'http://155.210.153.12:10012'   #'http://localhost:8069'
        XSERVER = request.env["ir.config_parameter"].get_param("server")
        ADMIN_PASSWORD = 'desarrollo'
        DATABASE = 'db4444'
        LOGIN = 'admin@tcm.com'
        USER_PASSWORD = 'desarrollo'
        LANG = 'es_CL'
        COUNTRY_CODE = 'cl'
        DEMO = False

        _logger.info('SERVER: %s', XSERVER)

        status = {}

        # client = erppeek.Client(server=SERVER)
        # if not DATABASE in client.db.list():
        #     print("La base de datos no existe, creando una!")
        #     client.create_database(ADMIN_PASSWORD, DATABASE, DEMO, LANG, USER_PASSWORD, LOGIN, COUNTRY_CODE)
        #     status['message'] = 'Instancia de Odoo (" % DATABASE % ") se creó con éxito!!!'
        #     print('Usuario: ', client.user)
        # else:
        #     print("La base de datos " % DATABASE % " ya existe.")
        #     status['message'] = "La base de datos (" % DATABASE % ") ya existe, por favor seleccione otro nombre."

        # Instalando los modulos necesarios
        # self.install_odoo_modules()
        print("Modulos instalados con exito!")

        ip_address = request.httprequest.environ['REMOTE_ADDR']
        print('IP del cliente: ', ip_address)

        # real_ip_address = request.httprequest.environ['HTTP_X_REAL_IP']
        real_ip_address = request.httprequest.environ.get('HTTP_X_REAL_IP')

        if (real_ip_address == None):
            pool_config = request.env['ir.config_parameter'].search([('key', '=', 'web.base.url')])[0]
            ip_server = pool_config.value
            print('IP del servidor: ', ip_server)
        else:
            print('IP real del servidor: ', real_ip_address)

        status['server'] = XSERVER
        status['ip_server'] = ip_server
        status['real_ip_address'] = real_ip_address

        return request.render("tcm_build_client.wizard_report", status)
        # Fin de la funcion
