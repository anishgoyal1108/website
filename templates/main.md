<%* 
const title = await tp.system.prompt("Title?"); 
const formattedTitle = title.replace(/[^\w\s]/gi, '').replace(/\s+/g, '-').toLowerCase();
type = await tp.system.prompt("Type?");
await tp.file.move(`content/${type}/${formattedTitle}.md`);
-%>
---
author: Anish Goyal
title: <% title %>
description: 
summary: 
eyeCatcher: 
tags: []
readingtime: 
---
<%*
tp.hooks.on_all_templates_executed(() => {
	app.workspace.activeLeaf.view.editor?.focus();
	app.commands.executeCommandById("obsidian-linter:lint-file");
}); 
-%>

## <% tp.file.cursor() %>