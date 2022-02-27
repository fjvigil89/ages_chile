$(document).ready(function () {
    var navListItems = $("div.setup-panel div a"),
        allWells = $(".setup-content"),
        allPrevBtn = $(".prevBtn"),
        allNextBtn = $(".nextBtn");

    allWells.hide();

    navListItems.click(function (e) {
        e.preventDefault();
        var $target = $($(this).attr("href")),
            $item = $(this);

        if (!$item.hasClass("disabled")) {
            navListItems.removeClass("btn-primary").addClass("btn-default");
            $item.addClass("btn-primary");
            $item.addClass("active");
            allWells.hide();
            $target.show();
            $target.find("input:eq(0)").focus();
        }
    });

    allPrevBtn.click(function () {
        var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            prevStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]')
                .parent()
                .prev()
                .children("a");

        prevStepWizard.removeAttr("disabled").trigger("click");
    });

    allNextBtn.click(function () {
        var curStep = $(this).closest(".setup-content"),
            curStepBtn = curStep.attr("id"),
            nextStepWizard = $('div.setup-panel div a[href="#' + curStepBtn + '"]')
                .parent()
                .next()
                .children("a"),
            curInputs = curStep.find(
                "input[type='text'],input[type='url'],input[type='password'],select"
            ),
            isValid = true;

        for (var i = 0; i < curInputs.length; i++) {
            $(curInputs[i]).closest(".form-control").removeClass("is-invalid");
            if (!curInputs[i].validity.valid || curInputs[i].selectedIndex == 0) {
                isValid = false;
                $(curInputs[i]).closest(".form-control").addClass("is-invalid");
            }
        }
        if (isValid) nextStepWizard.removeClass("disabled").trigger("click");
    });

    $("div.setup-panel div a.btn-primary").trigger("click");

    $(".radio-group .radio").click(function () {
        $(".selected .fa").removeClass("fa-check");
        $(".radio").removeClass("selected");
        $(this).addClass("selected");
    });

    //   $(".submit").click(function () {
    //     return false;
    //   });
});
