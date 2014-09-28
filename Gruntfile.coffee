module.exports = (grunt) ->
  template = @option("template" || 'default')
  static_path = @option("static" || '')

  fs = require 'fs'
  isModified = (filepath) ->
    now = new Date()
    modified =  fs.statSync(filepath).mtime
    return (now - modified) < 10000

  @initConfig
    watch:
      options:
        livereload: true
      template:
        files: ['templates/scss/*.scss', 'templates/coffee/*.coffee']
        tasks: ['compass:modified', 'coffee:modified']


    compass:
      options:
        sassDir: 'templates/scss/'
        cssDir: 'static/css/'
      compile:
        sassDir: 'templates/scss/'
        cssDir: 'static/css/'
      modified:
        cwd: 'templates/scss'
        src: '**/*.scss'
        dest: 'static/css'
        ext: '.css'
        filter: isModified

    coffee:
      options:
        sourceMap: true
        bare: true
        force: true
      modified:
        expand: true
        cwd: 'templates/coffee/'
        src: '**/*.coffee'
        dest: 'static/js/'
        ext: '.js'
        filter: isModified


  @loadNpmTasks("grunt-contrib-watch")
  @loadNpmTasks("grunt-contrib-compass")
  @loadNpmTasks("grunt-contrib-coffee")
  @registerTask "default", ["watch", "compass", "coffee"]
