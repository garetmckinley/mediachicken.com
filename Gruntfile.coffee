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
        files: ['mediachicken/templates/scss/*.scss', 'mediachicken/templates/coffee/*.coffee']
        tasks: ['compass:modified', 'coffee:modified']


    compass:
      options:
        sassDir: 'mediachicken/templates/scss/'
        cssDir: 'mediachicken/static/css/'
      compile:
        sassDir: 'mediachicken/templates/scss/'
        cssDir: 'mediachicken/static/css/'
      modified:
        cwd: 'mediachicken/templates/scss'
        src: '**/*.scss'
        dest: 'mediachicken/static/css'
        ext: '.css'
        filter: isModified

    coffee:
      options:
        sourceMap: true
        bare: true
        force: true
      compile:
        expand: true
        cwd: 'mediachicken/templates/coffee/'
        src: '**/*.coffee'
        dest: 'mediachicken/static/js/'
        ext: '.js'
      modified:
        expand: true
        cwd: 'mediachicken/templates/coffee/'
        src: '**/*.coffee'
        dest: 'mediachicken/static/js/'
        ext: '.js'
        filter: isModified


  @loadNpmTasks("grunt-contrib-watch")
  @loadNpmTasks("grunt-contrib-compass")
  @loadNpmTasks("grunt-contrib-coffee")
  @registerTask "default", ["watch", "compass", "coffee"]
