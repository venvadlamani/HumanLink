var gulp = require('gulp'),
    less = require('gulp-less'),
    sourcemaps = require('gulp-sourcemaps'),
    uglify = require('gulp-uglify'),
    concat = require('gulp-concat');

var paths = {
    js: 'app/**/*.js',
    less: 'assets/stylesheets/less/*.less'
};

gulp.task('move-less-dependencies', function () {

    return gulp.src([
        'bower_components/bootstrap/less/**/*.less',
    ])
        .pipe(gulp.dest('./assets/stylesheets/less/bootstrap/'));
});

gulp.task('compile-less', ['move-less-dependencies'], function () {
    return gulp.src([
        'assets/stylesheets/less/humanlink.less',
        'bower_components/pagepiling.js/jquery.pagepiling.css',
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
        'bower_components/pagepiling.js/jquery.pagepiling.min.js',
        'app/app.js',
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
