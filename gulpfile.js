var gulp        = require('gulp');
var browserify  = require('browserify');
var babelify    = require('babelify');
var source      = require('vinyl-source-stream');
var buffer      = require('vinyl-buffer');
var uglify      = require('gulp-uglify');
var sourcemaps  = require('gulp-sourcemaps');
var livereload  = require('gulp-livereload');


gulp.task('build', function () {
    return browserify({entries: './client/main.js', debug: true})
        .transform("babelify", { presets: ["es2015", "react", "stage-2"] })
        .bundle()
        .pipe(source('main.js'))
        .pipe(buffer())
        .pipe(sourcemaps.init())
        .pipe(uglify())
        .pipe(sourcemaps.write('./maps'))
        .pipe(gulp.dest('./server/assets/js/src'))
        .pipe(livereload());
});


gulp.task('watch', ['build'], function () {
    livereload.listen();
    gulp.watch('./client/*.js', ['build']);
    gulp.watch('./client/components/*.js', ['build']);
    gulp.watch('./client/components/Menu/*.js', ['build']);
    gulp.watch('./client/components/SideBar/*.js', ['build']);
    gulp.watch('./client/components/Pages/*.js', ['build']);
    gulp.watch('./client/components/Post/*.js', ['build']);
    gulp.watch('./client/components/Form/*.js', ['build']);
    gulp.watch('./client/actions/*.js', ['build']);
    gulp.watch('./client/reducers/*.js', ['build']);
    gulp.watch('./client/store/*.js', ['build']);
    gulp.watch('./client/auth/*.js', ['build']);
    gulp.watch('./client/api/*.js', ['build']);
});

gulp.task('default', ['build', 'watch']);
