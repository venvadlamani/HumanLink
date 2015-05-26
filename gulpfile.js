'use strict';

var gulp = require('gulp'),
    less = require('gulp-less'),
    minifyCss = require('gulp-minify-css'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat'),
    merge = require('merge-stream'),
    ngAnnotate = require('gulp-ng-annotate');

var paths = {
    js: 'app/**/*.js',
    less: 'assets/stylesheets/less/**/*.less'
};

var bundleJs = function (files, filename, annotate) {
    var g = gulp.src(files);
    g = g.pipe(concat(filename));
    if (annotate) {
        g = g.pipe(ngAnnotate({add: true}));
    }
    g = g.pipe(uglify());
    return g.pipe(gulp.dest('assets/js/build/'));
};

gulp.task('move-bootstrap', function () {
    var bower = 'bower_components';
    var less = gulp.src(bower + '/bootstrap/less/**/*.less')
                .pipe(gulp.dest('assets/stylesheets/less/bootstrap/'));
    var fonts = gulp.src(bower + '/bootstrap/fonts/*')
                .pipe(gulp.dest('assets/stylesheets/fonts/'));
    return merge(less, fonts);
});

gulp.task('compile-less', ['move-bootstrap'], function () {
    return gulp.src([
        'assets/stylesheets/less/humanlink.less'
    ])
        .pipe(concat('humanlink.css'))
        .pipe(less())
        .pipe(minifyCss({processImport: false}))
        .pipe(gulp.dest('assets/stylesheets/build/'));
});

gulp.task('compile-vendor', function() {
    var bower = 'bower_components';
    return bundleJs([
        bower + '/jquery/dist/jquery.js',
        bower + '/bootstrap/dist/js/bootstrap.js',
        bower + '/angular/angular.js',
        bower + '/angular-bootstrap/ui-bootstrap-tpls.js',
        bower + '/angular-ui-router/release/angular-ui-router.js',
        bower + '/checklist-model/checklist-model.js'
    ], 'vendor.js', false);
});

gulp.task('compile-js', function () {
    return bundleJs([
        'app/app.js',
        'app/*.js',
        'app/components/*/*module.js',
        'app/components/*/*.js',
        'app/components/*/*/*.js'
    ], 'humanlink.js', true);
});

gulp.task('compile', ['compile-less', 'compile-vendor', 'compile-js'],
          function() {
    // Do nothing.
});

gulp.task('watch', ['compile'], function() {
    gulp.watch(paths.js, ['compile-js']);
    gulp.watch(paths.less, ['compile-less']);
});

gulp.task('default', ['watch'], function () {
    // Do nothing.
});

