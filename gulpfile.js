const gulp = require("gulp");
const sass = require("gulp-sass")(require("sass"));
const watch = require("gulp-watch");

gulp.task("sass", function () {
  return gulp
    .src("assets/scss/main.scss")
    .pipe(sass().on("error", sass.logError))
    .pipe(gulp.dest("assets/css/"));
});

gulp.task("watch", function () {
  watch("assets/scss/*.scss", gulp.series("sass"));
});

gulp.task("default", gulp.series("sass", "watch"));
