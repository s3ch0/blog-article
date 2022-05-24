## HTML


### 浮动

通过浮动可以使一个元素向其父元素的左侧或右侧移动

使用 `float`属性来设置元素的浮动

可选值:

+ `none` 默认值:元素不浮动
+ `left` 元素向左浮动
+ `right` 元素向右浮动

> 元素设置浮动以后,水平布局的等式便不需要强制成立

元素设置浮动以后,会完全脱离文档流中脱离,不再占用文档流的位置

所以元素下边的还在文档流中的元素会自动向上移动

浮动的特点:

1. 浮动元素会完全脱离文档流,不再占据文档流中的位置
2. 设置浮动以后元素会向父元素的左侧或右侧移动
3. 移动元素默认不会从父元素中移出
4. 浮动元素向左或向右移动时,不会超过它前边的其他浮动元素
5. 如果浮动元素的上边是一个没有浮动的块元素,则浮动元素无法上移
6. 浮动元素不会超过它上边的浮动的兄弟元素,最多就是和它一样高

> 浮动主要作用就是让页面中的元素可以水平排列,通过浮动可以制作一些水平方向的布局



浮动元素不会盖住文字,文字会自动环绕在浮动元素的周围,所以我们可以利用浮动来设置*文字环绕图片的效果*

从文档流中脱离以后,元素的一些特点也会发生变化

**脱离文档流的特点:**

块元素:

1. 块元素不在独占页面的一行
2. 脱离文档流以后,块元素的宽度和高度默认都被内容撑开

行内元素:

1. 行内元素脱离文档流以后会变成块元素,特点和块元素一样

脱离文档流以后,不再区分块和行内元素了

高度塌陷

在浮动布局中,父元素的高度默认是被子元素撑开的

当子元素浮动后,其会完全脱离文档流,子元素从文档流中脱离

将会无法撑起父元素的高度,导致父元素的高度丢失

父元素高度丢失以后,其下的元素会自动上移,导致布局混乱

所以高度塌陷是浮动布局中比较常见的一个问题,这个问题我们必须要进行处理

> BFC(Block Formatting Context) 块级格式化环境

+ BFC是CSS中的一个隐含的属性,可以为一个元素开启BFC 开启BFC该元素会变成一个独立的布局区域


元素开启BFC后的特点

+ 开启BFC的元素不会被浮动元素所覆盖
+ 开启BFC的元素子元素和父元素外边距不会重叠
+ 开启BFC的元素可以包含浮动的子元素

---

我们可以通过一些特殊方式来开启元素的BFC

1. 设置元素的浮动 (不推荐)
2. 将元素设置为行内块元素 (不推荐)
3. 将元素的`overflow`设置为一个非`visible`的值 
   + 常用的方式 为元素设置 `overflow:hidden;` 开启BFC 以使其可以包含浮动元素





使用`after` 伪类来解决高度塌陷

```css
.box1::after
{
    content:'';
    display:block;
    /* ::after伪类默认为行内元素 */
    clear:both;
}
```



外边距折叠

```css
.box1::before{
    content:'';
    display:table;
}
```

`clearfix` 这个样式可以同时解决高度塌陷和外边距重叠的问题

```css
.clearfix::before,
.clearfix::after{
    content:'';
    display:table;
    clear:both;
}

  <div class="box1 clearfix">
            <div class="box2"></div>
  </div>
```

### 定位

定位:`position`是一种更加高级的布局手段

通过定位可以将元素摆放到页面的任意位置

使用`position`属性来设置定位

可选值:

+ `static` 默认值 元素是静止的,没有开启定位
+ `relative` 开启元素的相对定位
+ `absolute` 开启元素的绝对定位
+ `fixed` 开启元素的固定定位
+ `sticky` 开启元素的粘滞定位

#### 相对定位

当元素的`position`属性值设置为`relative`时则开启了元素的相对定位

相对定位的特点:

+ 元素开启相对定位以后,如果不设置偏移量元素不会发生任何的变化
+ 

> 偏移量(offset) 当元素开启了定位以后,可以通过偏移量来设置元素的位置

+ top
+ bottom
+ left
+ right

### flex布局

> 开启`flex`布局:在`css/wxss`用css选择器选择对应的元素后 *display:flex* 就算开启了flex布局 

```css
.menu{
    display: flex;
    flex-direction: row; /*指定排序的方式*/ 
    justify-content: space-around;
}
.menu .item{
    display:flex;
    flex-direction:column;
    align-items:center; 
    /*将容器内的小元素居中(里面得到文本)*/
}
```

1. **`flex-direction:` 规定主轴的方向**

   + `row` ：规定主轴方向为水平方向
   + `column`：规定主轴方向为竖直方向

2. **`justify-content \ align-items:` 元素在主轴\副轴方向如何展示 ( 排列 )**

   + `flex-start` ：默认的 ( 元素从左/上开始排列 )
   + `center`：元素居中排列
   + *`space-around` ：元素在页面内均匀排列* 
   + `space-between`：界面两端的元素贴着界面,中间得到元素均匀排列

   + `flex-end`：元素从右/下开始排列



### 图标字体

图标字体（iconfont）

1. 在网页中经常需要使用一些图标，可以通过图片来引入图标

2. 但是图片大小本身比较大，并且非常的不灵活,所以在使用图标时，我们还可以将图标直接设置为字体，

3. 然后通过font-face的形式来对字体进行引入这样我们就可以通过使用字体的形式来使用图标

`fontawesome` 图标字体库的使用步骤

1. 下载 https://fontawesome.com/

2. 解压

3. 将`css`和`webfonts`移动到项目中

4. 将all.css引入到网页中

5. 使用图标字体

+ 直接通过类名来使用图标字体

        ```html
        <!-- class="fas fa-bell" -->
        <!-- class="fab fa-accessible-icon" -->
        <i class="fas fa-bell" style="font-size:80px; color:red;"></i>
        <i class="fas fa-bell-slash"></i>
        <i class="fab fa-accessible-icon"></i>
        <i class="fas fa-otter" style="font-size: 160px; color:green;"></i>
        ```



其他方式使用图标字体

```css
li::before{
            /* 
                通过伪元素来设置图标字体
                    1.找到要设置图标的元素通过before或after选中
                    2.在content中设置字体的编码
                    3.设置字体的样式
                        fab
                        font-family: 'Font Awesome 5 Brands';
    
                        fas
                        font-family: 'Font Awesome 5 Free';
                        font-weight: 900; 
            */
    
            content: '\f1b0';
            /* font-family: 'Font Awesome 5 Brands'; */
            font-family: 'Font Awesome 5 Free';
            font-weight: 900; 
            color: blue;
            margin-right: 10px;
        }
```



```html
 <!--  通过实体来使用图标字体： &#x图标的编码;-->
    <span class="fas">&#xf0f3;</span>
```





阿里图标字体

```css
 <style>
        i.iconfont{
            font-size: 100px;
        }

        p::before{
            content: '\e625';
            font-family: 'iconfont';
            font-size: 100px;
        }
 </style>
```



```html


<body>

    <i class="iconfont">&#xe61c;</i>
    <i class="iconfont">&#xe622;</i>
    <i class="iconfont">&#xe623;</i>

    <i class="iconfont icon-qitalaji"></i>

    <p>Hello</p>
</body>
```



### 其他

将`li`标签前的小原点去掉

`list-style-type: none;`

将字垂直居中：将`line-height` 的大小设置为与父元素容器的大小



优化input样式

设置 outline-style: none ; 取消外边框

将文字在父元素中垂直居中

`line-height:父元素的高度;`



将a标签的下划线去除

`text-decoration:none;`



#### vscode

<kbd>ctrl</kbd>+<kbd>shift</kbd>+<kbd>I</kbd> : 格式化代码





### CSS



### JS



浏览器中的JavaScript有三个要素

+ ECMAScript  -- ES  -- 语法规范 （关键字，运算符，分支，循环，对象，函数）

+ BOM -- Browser Object Model -- 浏览器对象模型 -- window

  + `location / history / screen / navigator`
  + `alert() / prompt() / confirm() / open() / close()`
  + `setTimeot() / setInterval()`

+ DOM -- Document Object Model -- 文档对象模型 -- document

  + `querySelector() /querySelectorAll()`   -- 根据CSS选择器获取页面上的标签

  + `createElement()`    -- 创建新标签
  + `appendChild() / insertBefore()`  -- 添加新标签
  + `removeChild()`   -- 删除标签
  + `textContent / innerHTML`    -- 修改标签内容
  + `style`   -- 修改标签样式









```js

// document对象的querySelector和querySelectorAll 可以通过CSS选择器获取页面元素，前者获取第一个出现的元素，后者获取元素的列表



```



[Bootcdn.cn](https://www.bootcdn.cn/)

JSON: JavaScript Object Notation



后端渲染：通过后端代码（Java，Python，PHP等）渲染模板页面为页面生成动态内容

缺点：

+ 搞后端的人还需要具备一些前端的知识
+ 开销比较大，增加服务器的负担和压力

前端渲染：后端是负责处理业务和提供数据，前端实现页面的渲染

优点：

+ 前后端的工作是独立的，相互不影响
+ 通过浏览器中的JavaScript引擎实现页面渲染，不增加服务器负担



Python程序会提供JSON格式的数据，前端通过JavaScript请求JSON数据

获得数据后通过Vue.js实现页面的渲染 （把数据动态填写到页面上）

[MDN: 前端文档](https://developer.mozilla.org/zh-CN/)

## Flask




`sprite animation`
