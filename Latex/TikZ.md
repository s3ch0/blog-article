学习 TikZ 我们可以使用以下网站
http://www.texample.net/tikz/examples

```latex
% !TEX program = xelatex
\documentclass{ctexart}
\usepackage{amsmath,mathrsfs,amsfonts}
\usepackage{tikz}
\usepackage{graphicx}

% library

\begin{document}

\begin{figure}[htp]
    \centering

% > = latex/stealth
\begin{tikzpicture}[>=stealth]
\draw[|-|,thick] (0,0)--node[below=0.01mm]{5cm}(5,0);
% abrove/below

% thick,very thick ,ultra thick
% thin
\draw[->|,dotted] (0,-1) to (5,-1);
\draw[dashed] (0,-2) to (5,-2);
\draw[dashdotted] (0,-3) to (5,-3);

\end{tikzpicture}    
    \caption{}
\end{figure}


\begin{figure}[htp]
    \centering
    \begin{tikzpicture}
        
    \end{tikzpicture}
    \caption{}
\end{figure}

\end{document}


```





```latex
\begin{figure}[htp]
    \centering
    \begin{tikzpicture}[>=latex]
        \draw[->] (-1,0)--(4,0)node[right]{$x$};
        \draw[->] (0,-1)--(0,4)node[right]{$y$};
        % \draw (0,2)node[left]{$N$}--(2,2)node[right]{$P(x,y)$}--(2,0)node[below]{$M$};
        \node at (-0.2,-0.2){$O$};
        %\draw (1,0)node[below]{$1$}--(1,.1);
        % \draw (0,1)node[left]{$1$}--(.1,1);
        
        \foreach \y in {1,2,...,6}
        {
            \draw (0,\y*0.5)node[left]{$\y$}--(.1,\y*0.5);
            \draw (\y*0.5,0)node[below]{$\y$}--(\y*0.5,.1);
        }
        

    \end{tikzpicture}
    \caption{}
\end{figure}
```


