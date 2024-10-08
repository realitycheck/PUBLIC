1. go to /usr/share/code/resources/app/out/vs/workbench
2. find workbench.desktop.main.css
3. add to the bottom
```
/* SidePanel */
:root {
	/* you can change these values */
 --vscode-pane-view-font-family: "Go Mono";
 --vscode-pane-view-font-size: 15px;
}
.monaco-pane-view {
font-family: var(--vscode-pane-view-font-family);
font-size: var(--vscode-pane-view-font-size) !important;
}
.monaco-pane-view h3 {
font-family: var(--vscode-pane-view-font-family);
font-size: calc(var(--vscode-pane-view-font-size) - 2px) !important;
}
.monaco-highlighted-label {
font-family: var(--vscode-pane-view-font-family);
font-size: calc(var(--vscode-pane-view-font-size) - 1px) !important;
}
.monaco-workbench .monaco-list-row .expression .value {
font-family: var(--vscode-pane-view-font-family);
font-size: calc(var(--vscode-pane-view-font-size) - 1px) !important;
}
```
4. chmod 444 workbench.desktop.main.css 
