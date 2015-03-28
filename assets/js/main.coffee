---
---
$ ->
  nav = $("#navigation")
  previous = 0
  tick = 0
  frozen = 0

  minifyNav = ->
    s = 36
    $("#navigation").addClass "sticky"
    $(".header-spacer").addClass "sticky"

  handleScroll = ->
    scroll = window.pageYOffset
    navPos = $("#navigation").offset().top
    distance = scroll - navPos

    if (distance < previous - tick or distance > previous + tick)
      if (-distance >= 36 and -distance < 330)
        previous = distance
        s = -(distance)*.90
      else if scroll <= frozen
        if $("#navigation").hasClass "sticky"
          $("#navigation").removeClass "sticky"
          $(".header-spacer").removeClass "sticky"
      else if -distance <= 0 and not $("#navigation").hasClass "sticky"
        frozen = 340
        previous = frozen
        minifyNav()


  $("#navigation").width $(".container").width()
  $(window).resize ->
    $("#navigation").width $(".container").width()

  $(window).scroll ->
    handleScroll()
