var gulp = require('gulp'),
    less = require('gulp-less'),
    sourcemaps = require('gulp-sourcemaps'),
    concat = require('gulp-concat');

gulp.task('compile-less', function () {
    gulp.src([
        'bower_components/bootstrap/less/bootstrap.less'
    ])
        .pipe(sourcemaps.init())
        .pipe(less())
        .pipe(sourcemaps.write())
        .pipe(concat('new-bootstrap.css'))
        .pipe(gulp.dest('./assets/stylesheets/build/'));
});

gulp.task('default', ['compile-less'], function () {

});
