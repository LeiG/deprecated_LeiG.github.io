Title: 用Pelican在Github上创建个人博客
Date: 2016-01-01 17:25
Modified: 2016-01-10 18:37
Category: misc
Tags: pelican, git
Slug: set-up-github-page-with-pelican
Authors: Lei Gong

2016年第一天，折腾了一个下午，终于在Github上建立好了自己的博客，希望从今年开始好好记录自己的学习过程，也能和大家多交流！开博第一篇就用来总结下我是如何用Pelican在Github上创建了这个博客，算是自己的一个回顾，要是凑巧能给和我一样的初学者提供一点帮助那真是额外的惊喜了。

## Set up a github.io page

首先自然是要注册一个Github的账号。Github是目前最火的开源社区，它建立于git的基础之上，提供了方便的source control工具和一个强大的开源平台。目前，几乎你能在上面找到所有目前活跃的开源项目的repo。之外，它还给我们提供了Github Pages这样的平台来host我们的个人页面。

要建立一个新的Github Page，我们第一步需要创建一个新的repo，并以username.github.io来命名。这样我们就方便的建立了一个Github User Page（另有Github Project Page， 感兴趣的朋友可以Google之）。

Github User Page会display任何在master branch上的东西。这里我假设了大家都对git有初步的了解，如果觉得有困难可以花几分钟学习一下这个简短实用的[git教程](https://try.github.io/levels/1/challenges/1)。为了方便后面的步骤，我们需要先新建并切换到一个新的git分支`source`，这也是以后我们主要的工作分支。

```
$ git checkout -b source
```

## Install Pelican

Pelican是基于Python搭建的blog系统。我们可以简单的用`pip install`来完成安装，但是一个良好的开发习惯是把每个项目封装在自己的virtual environment里，这样会省去很多以后维护的麻烦。注意我用的版本是Python2.7，不过Python3应该也能用基本一样的办法安装。

```
$ pip install virtualenv
$ cd username.github.io/
$ virtualenv venv
$ source venv/bin/activate
```

这样我们就建立并且激活了这个叫做`venv`的virtual environment了。你自然用不着commit这个文件夹，所以不要忘记把它添加到你的`.gitignore`里咯。

接下来让我们正式来安装Pelican和一些必要的组件（注意我们已经在venv这个环境里了）。

```
(venv)$ pip install pelican markdown
```

非常幸运地，Pelican提供了一种非常简便的方式来新建一个项目，你只需要回答一些yes/no的问题就可以设置了。

```
(venv)$ pelican-quickstart
```

## Create your first post

一切就绪，现在我们终于可以来写第一篇博客了（以后就可以直接从这一步开始咯）。我喜欢用markdown这种格式来编辑博文，因为它非常简单而且轻巧。所有的`.md`后缀的博文都存在`content`这个文件夹下，用你最喜欢的编辑器新建一篇就可以了。

```
(venv)$ vim content/test.md
```

下面是一个比较实用的博文模版，你可以选择从这个格式开始。

```
My super title
##############

:date: 2010-10-03 10:20
:modified: 2010-10-04 18:40
:tags: thats, awesome
:category: yeah
:slug: my-super-post
:authors: Alexis Metaireau, Conan Doyle
:summary: Short version for index and feeds
```

写完了一篇博客，我们还需要重新generate整个site到`output`这个文件夹里。这一步也一贯的简单，在site的根目录下执行下面这行代码就可以了。

```
(venv)$ pelican content
```

## Commit to Github

完成了本地的编辑，最后一步是把内容push到master branch上，不过在这之前，我们还需要另外一个设置。因为Github User Page会display任何在master上的内容，而其实我们真正需要的只是`output`这个文件夹。当然你可以只push这个文件夹到master，但已经有一个非常好用的script能把这一步自动化了。

```
(venv)$ pip install ghp-import
```

有了这个script，我们只需要按次序执行下面这几行命令就可以把所有的东西都按类push到远程，而且我们的blog也会上线啦。

```
(venv)$ git branch gh-pages
(venv)$ ghp-import output
(venv)$ git checkout master
(venv)$ git merge gh-pages
(venv)$ git push --all
```

总结一下，我们最后有三个git分支，其中`source`是主要的工作分支，`master`是真正host博客的分支，`gp-pages`像是它们之间的搬运工。

```
  gh-pages
  master
* source
```

## Settings

这里我只是进行了一些最基本的设置，为了让你的博客更美观，更丰富，最主要的是更个性，你需要修改一下site根目录下的`pelicanconf.py`文件，也可以从[Github/pelican-themes](https://github.com/farseerfc/pelican-themes)上选择一些主题。总之，有很多可以尝试和优化的，希望这篇能当作一个敲门砖。
