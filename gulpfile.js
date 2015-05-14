'use strict';

var gulp = require('gulp'),
    less = require('gulp-less'),
    sourcemaps = require('gulp-sourcemaps'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    merge = require('merge-stream');

var paths = {
    js: 'app/**/*.js',
    less: 'assets/stylesheets/less/**/*.less'
};

gulp.task('move-bootstrap-dependencies', function () {
    var less = gulp.src('bower_components/bootstrap/less/**/*.less')
        .pipe(gulp.dest('./assets/stylesheets/less/bootstrap/'));
    var fonts = gulp.src('bower_components/bootstrap/fonts/*')
        .pipe(gulp.dest('./assets/stylesheets/fonts/'));
    return merge(less, fonts);
});

gulp.task('compile-less', ['move-bootstrap-dependencies'], function () {
    return gulp.src([
        'assets/stylesheets/less/humanlink.less',
    ])
        .pipe(sourcemaps.init())
        .pipe(less())
        .pipe(sourcemaps.write())
        .pipe(concat('style.css'))
        .pipe(gulp.dest('./assets/stylesheets/build/'));
});

gulp.task('compile-js', function() {
    return gulp.src([
        'bower_components/jquery/dist/jquery.js',
        'bower_components/bootstrap/dist/js/bootstrap.js',
        'bower_components/angular/angular.js',
        'bower_components/angular-bootstrap/ui-bootstrap-tpls.js',
        'bower_components/angular-ui-router/release/angular-ui-router.js',
        'bower_components/checklist-model/checklist-model.js',
        'app/app.js',
        'app/*.js',
        'app/components/*/*module.js',
        'app/components/*/*.js',
        'app/components/*/*/*.js',
    ])
        .pipe(sourcemaps.init())
        .pipe(concat('scripts.min.js'))
        .pipe(uglify())
        .pipe(sourcemaps.write())
        .pipe(gulp.dest('./assets/js/build/'));
});

gulp.task('watch', function() {
    gulp.watch(paths.js, ['compile-js']);
    gulp.watch(paths.less, ['compile-less']);
});

gulp.task('default', ['watch', 'compile-less', 'compile-js'], function () {
    // Do nothing.
});

gulp.task('compile', ['compile-less', 'compile-js'], function() {
    // Do nothing.
});
