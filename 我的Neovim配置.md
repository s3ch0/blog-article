![20220208_2320.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/4bbca5ec972cfc1ad9ac072b2d97047a.png)


# 打造属于自己的 vim


> 我的 vim 配置文件存放地址：[init.vim](https://gitee.com/zhouhaohub/myutil)





### coc-vim 

![20220208_2203.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/c59ef21addb4d2d52bbea891e5e2ad27.png)



#### 安装coc本体

安装 nodejs >=12.12
> 安装完node之后就有它的包管理器 npm
```bash
curl -sL install-node.vercel.app/lts | bash
```

使用 vim-plug 安装 coc

```vim
" Use release branch (recommend)
Plug 'neoclide/coc.nvim', {'branch': 'release'}

" Or build from source code by using yarn: https://yarnpkg.com
Plug 'neoclide/coc.nvim', {'branch': 'master', 'do': 'yarn install --frozen-lockfile'}
" 记得执行 ：PlugInstall
```
> 如果因为网的问题 第一次没有安装成功,可以多尝试几次 Pluginstall

安装完之后，可以执行 :checkhealth 来查看是否成功安装,如果在coc列表那么不是全部ok的话,再去确认一下是否成功安装了node npm ...
> :checkhealth 好像只能在nvim里面执行，如果是vim用户的话可以使用 :CocInfo

![20220209_1819.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/065328b806295c3c5519c527aa4993ce.png)


#### 安装coc扩展
我们可以使用 `:CocInstall` 来安装我们所需要补全的语言

```vim
" 安装 json 代码的自动补全
:CocInstall coc-json

" 卸载 coc-json
:CocUninstall coc-json
```
<font color="red" face=Monaco size=3> 查看我们下载了哪些 coc 扩展 </font>

```vim
:CocList extensions
" 当我们选中了这个插件之后，我们可以按一下 tab 键来对该语言插件进行一系列操作
```
> 在列出的插件中，* 为已经启用 + 代表在当前文件内并未启用。
![20220209_1840.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/902fdc11b3c50154b46a1e2b7638118d.png)



当然我们使用上面这种方式，如果有多台计算机的话，还是要在每个计算机上都要执行上面的安装命令，所以相对来说会比较麻烦，所以我们可以使用以下方式来达到一次配置，多台机器可用的效果
> 我们可用使用修改 vim 配置文件的方式
配置项格式为：
```vim
" 使用此配置来指定安装什么 coc 插件
let g:coc_global_extensions = [
	\'coc-json',
	\'coc-vimlsp']
```
当配置完上面的配置之后,退出 vim 再重新启动后，coc就会自动安装配置文件里指定的插件.

> 这时你可能会有一个疑问！我怎么知道对应语言应该安装哪个插件 :laughing:

我们可以使用下面这个 coc 插件来缓解一下这个问题.当然你也可以 stfw rtfm :joy:

```vim
:CocInstall coc-marketplace
" 安装完之后我们可以使用一下命令来查找你所需要的插件
:CocList marketplace

```

#### coc补全与配置
当你已经安装好了自己想要 coc 插件，这时候就可以使用 coc 来进行代码补全啦！:smile:
如果你没配置 coc 的话，你会发现一个严重的问题，那就是但我想要补全时，按了一下  <kbd class="keybord"> tab </kbd>&ensp;键，你会发现 coc 并没有给你补全对应的代码，而仅仅就是打印了一个 tab 
<font color="red" face=Monaco size=3> 为了更好地使用 coc 所以我还是推荐大家进行以下配置(也是我的常用配置): </font>
> 我还会对一下重要配置进行一些说明！

```vim

set hidden
set updatetime=100 " 文档上为300 让coc响应更快一点
set shortmess+=c   " 让coc补全窗口少显示一点没用的东西
" set signcolumn=number 将左边的 coc 提示栏与行号栏合在一起 

" ------------------------------------
" 解决上面提到的 按 tab 键并>不能实现补全的效果
inoremap <silent><expr> <TAB>
      \ pumvisible() ? "\<C-n>" :
      \ <SID>check_back_space() ? "\<TAB>" :
      \ coc#refresh()
inoremap <expr><S-TAB> pumvisible() ? "\<C-p>" : "\<C-h>"

function! s:check_back_space() abort
  let col = col('.') - 1
  return !col || getline('.')[col - 1]  =~# '\s'
endfunction
" ------------------------------------

" 在插入模式下按 ctrl + o 打开 coc 代码补全界面
" 默认为 ctrl + space ，而我习惯于 ctrl + o 在普通模式下按 ctrl + o 为回到上个位置
inoremap <silent><expr> <c-o> coc#refresh()


" 当选中 coc 要补全的代码，然后按一下回车就会展开所选中的代码块 
inoremap <silent><expr> <cr> pumvisible() ? coc#_select_confirm()
                              \: "\<C-g>u\<CR>\<c-r>=coc#on_enter()\<CR>"

" 使用 [g 和 ]g 来跳转至 coc上一个报错和下一个报错的地方 
nmap <silent> [g <Plug>(coc-diagnostic-prev)
nmap <silent> ]g <Plug>(coc-diagnostic-next)

" 对变量函数...进行定义,类型,引用等跳转
nmap <silent> gd <Plug>(coc-definition)
nmap <silent> gD :tab sp<CR><Plug>(coc-definition)
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references)

" ------------------------------------
" 按<LEADER> + h 查看帮助文档
nnoremap <LEADER>h :call <SID>show_documentation()<CR>

function! s:show_documentation()
  if (index(['vim','help'], &filetype) >= 0)
    execute 'h '.expand('<cword>')
  elseif (coc#rpc#ready())
    call CocActionAsync('doHover')
  else
    execute '!' . &keywordprg . " " . expand('<cword>')
  endif
endfunction
" ------------------------------------

" 当光标停留在变量上时，让与其名字一样的变量都高亮显示
" 不行的话 安装一下 coc-heighlight
autocmd CursorHold * silent call CocActionAsync('highlight')

" Applying codeAction to the selected region.
" Example: `<leader>aap` for current paragraph
xmap <leader>a  <Plug>(coc-codeaction-selected)
nmap <leader>a  <Plug>(coc-codeaction-selected)
```

#### `coc-settings.json`
我们可以使用 `:CocConfig` 这个命令来打开并用默认编辑器编辑 coc-settings.json 这个文件
我的 `coc-settings.json` 文件: [coc-settings.json](https://gitee.com/zhouhaohub/myutil) 

> 下面我来对这个配置进行一些说明
<font color="red" face=Monaco size=3> 对于下面的配置，我们都可以使用 `:help coc-nvim` 来查看其含义</font>

```json

{
	# 让coc每天自动检测更新,当然我们还可以设置别的值如never 
	"coc.preferences.extensionUpdateCheck": "daily",
	# 下面这两行就是让我们在使用 coc 补全时，在我们没有按 tab 选中我们需要补全的内容时按回车不会自动补全代码
	"suggest.noselect": true,
	"suggest.enablePreselect": false,
	


}



```




#### 不同编程语言的配置


#### 其他coc扩展


#### 创建简单的coc扩展













<font color="red" face=Monaco size=3>在vim中使用单词翻译 </font>

> sdcv全称为stardict console version，

1. 安装 `sdcv`
```bash
# install the sdcv
sudo apt-get install sdcv # ubuntu
sudo pacman -S sdcv # arch
```
2. 下载词典数据
> 下载词典数据，之前其实只是安装了不带词典数据的 sdcv
字典下载地址是：[Dictionary Links](http://download.huzheng.org/)
这边我使用的是: 朗道英汉字典 `langdao-ec-gb dictionary(en - zh_CN)`
[Download](http://download.huzheng.org/zh_CN/stardict-langdao-ec-gb-2.4.2.tar.bz2)

3. 将词典压缩包解压到 `/usr/share/stardict/dic` 目录下
> 如果没有此目录则手工创建

```bash
# 解压命令
tar xf source.tar[.gz|.bz2|.xz]
```
4. 此时可以在 `shell` 终端下进行查询
```bash
sdcv -l # 列出安装了哪些字典
sdcv hello
```
5. 配置 `vim/neovim`

在使用下面这些配置前必须要确保系统中装有sdcv
```vim
set keywordprg=sdcv\ -u\ 朗道英汉字典5.0 " 这边的字典要看你安装了什么
function! MySdcv()
    let retStr=system('sdcv '.expand("<cword>"))
    windo if expand("%")=="dictWin" |q!|endif
    30vsp dictWin
    setlocal buftype=nofile bufhidden=hide noswapfile
    1s/^/\=retStr/
    1
endfunction

map F :call MySdcv()<CR>

```
> 如果你使用上面这个配置的话,你只需要在要翻译的单词上按一下 <kbd class="keybord"> Shift </kbd> + <kbd class="keybord"> k </kbd>&ensp;即可

![20220209_0147.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/e27a5d73d87279cac2f35373e40b398c.png)

### 在 vim 里写markdown

![20220208_2210.png](http://zhouhao-blog.oss-cn-shanghai.aliyuncs.com/articles/29fa3b95e1c350c047fd0c621f9410e2.png)

