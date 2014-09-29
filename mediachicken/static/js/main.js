$(function() {
  var frozen, handleScroll, minifyNav, nav, previous, svg, tick;
  svg = $("#logo");
  nav = $("#navigation");
  previous = 0;
  tick = 0;
  frozen = 0;
  minifyNav = function() {
    var s;
    s = 36;
    $("#logo").width(s);
    $("#logo").css("margin-left", -s / 2 + "px");
    $("#navigation").addClass("sticky");
    return $(".header-spacer").addClass("sticky");
  };
  handleScroll = function() {
    var distance, navPos, s, scroll;
    scroll = window.pageYOffset;
    navPos = $("#navigation").offset().top;
    distance = scroll - navPos;
    if (distance < previous - tick || distance > previous + tick) {
      if (-distance >= 36 && -distance < 330) {
        if ($("#logo").hasClass("fullsize")) {
          $("#logo").removeClass("fullsize");
        }
        previous = distance;
        s = -distance * .90;
        $("#logo").width(s);
        return $("#logo").css("margin-left", -s / 2 + "px");
      } else if (-distance >= 330) {
        $("#logo").addClass("fullsize");
        s = 325;
        $("#logo").width(s);
        return $("#logo").css("margin-left", -s / 2 + "px");
      } else if (scroll <= frozen) {
        if ($("#navigation").hasClass("sticky")) {
          $("#navigation").removeClass("sticky");
          return $(".header-spacer").removeClass("sticky");
        }
      } else if (-distance <= 0 && !$("#navigation").hasClass("sticky")) {
        frozen = 340;
        previous = frozen;
        return minifyNav();
      }
    }
  };
  $("#navigation").width($(".container").width());
  $(window).resize(function() {
    return $("#navigation").width($(".container").width());
  });
  return $(window).scroll(function() {
    return handleScroll();
  });
});

//# sourceMappingURL=main.js.map
