$(document).ready(function() {
    // $.ajax({
    //     type: "POST",
    //     url: `/india`,
    //     data: {},
    //     contentType: "application/json;charset=UTF-8",
    //     success: function(res) {
    //         console.log(res)
    //         window.info = JSON.parse(res)
    //     },
    //     complete: function() {
    //         $(".loading").hide()
    //         for (var city in window.info) {
    //             console.log(city)
    //             $("#city").append(`<option value="${city}">${city}</option>`)
    //         }
    //         $("#city").change(function(){
    //         	$(".data").text(JSON.stringify(window.info[$("#city").val()]))
    //         })
    //         $(".btn").click(function() {
    //             $(".data").text(JSON.stringify(window.info[$(".inp").val()]))
    //         })
    //     }
    // })
    $.ajax({
        type: "POST",
        url: `/usa`,
        data: {},
        contentType: "application/json;charset=UTF-8",
        success: function(res) {
            console.log(JSON.parse(res))
            window.info = JSON.parse(res)
        },
        complete: function() {
            $(".loading").hide()
            for (var city in window.info["states"]) {
                console.log(city)
                $("#city").append(`<option value="${city}">${city}</option>`)
            }
            $("#city").change(function(){
            	$(".data").text(JSON.stringify(window.info.states[$("#city").val()]["totalcases"]))
            })
            $(".btn").click(function() {
                $(".data").text(JSON.stringify(window.info[$(".inp").val()]))
            })
        }
    })	
})