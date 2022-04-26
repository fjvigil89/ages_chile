/* Plantilla HTML */
var htmlCodePlanPasico =
    '<strong>Plan Basico Contratado</strong><br/>' +
    '1 Usuario, Administrador de la APP<br/>' +
    '1 Usuario, POS de Venta<br/>' +
    'Emision de Boleta Electronica<br/>' +
    'Emision y Recepcion de DTE:<br/>' +
    '<ul>' +
    '<li>Factura Electronica</li>' +
    '<li>Notas de Credito y Debito</li>' +
    '</ul>' +
    '</ul>' +
    'Gestion de Productos<br/>' +
    '<ul>' +
    '<li>Maestro de Productos</li>' +
    '<li>Precio de Compra</li>' +
    '<li>Precio de Venta</li>' +
    '</ul>' +
    'Gestion de Socios Comerciales<br/>' +
    '<ul>' +
    '<li>Clientes</li>' +
    '<li>Proveedores</li>' +
    '</ul>';


var htmlCodePlanAdicional =
    '<strong>APP Adicionales</strong><br/>' +
    '1 POS Adicional<br/>' +
    '2 Empleados para RRHH<br/>' +
    '1 Pagina Web e-Commerce<br/>' +
    '1 Usuario Gestion de Bodegas<br/>' +
    '1 Bodega o Sala de Ventas';


var htmlCodeTotal =
    '<table cellspacing="1" cellpadding="1">' +
    '<tr>' +
    '<th>Total Usuario Contratados</th>' +
    '<th>5</th>' +
    '</tr>' +
    '<tr>' +
    '<td>Usuario Administrador</td>' +
    '<td>1</td>' +
    '</tr>' +
    '<tr>' +
    '<td>Usuario Caja (POS)</td>' +
    '<td>1</td>' +
    '</tr>' +
    '<tr>' +
    '<td>Usuario Contador</td>' +
    '<td>0</td>' +
    '</tr>' +
    '<tr>' +
    '<td>Usuario Compras</td>' +
    '<td>1</td>' +
    '</tr>' +
    '<tr>' +
    '<td>Usuario RRHH</td>' +
    '<td>1</td>' +
    '</tr>' +
    '<tr>' +
    '<td>suario Inventario</td>' +
    '<td>1</td>' +
    '</tr>' +
    '</table>';

var htmlBasico = $.parseHTML(htmlCodePlanPasico);
var htmlAdicional = $.parseHTML(htmlCodePlanAdicional);
var htmlSummary = $.parseHTML(htmlCodeTotal);
$("#planBasico").append(htmlBasico);
$("#planAdicional").append(htmlAdicional);
$("#totales").append(htmlSummary);

//var template = $("#template1").html();
//var $row = $(template);

// Add the row to the table
//$("#resumenPlan").append($row);