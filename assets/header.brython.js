__BRYTHON__.use_VFS = true;
var scripts = { 
    "$timestamp": 1697817727415, 
    "header": [".py", 
    "from browser import bind,console,html,window,document,alert\n" +
    "import browser.widgets.menu as menu\n\n" +
    "import sys\n" +
    "version=f'{sys.implementation.version.major}.{sys.implementation.version.minor}'\n\n" +
    "href=document.location.href\n" +
    "protocol,rest=href.split(\"://\")\n" +
    "host,addr=rest.split(\"/\",1)\n\n\n" +
    "if protocol ==\"http\"and host.endswith(\"brython.info\"):\n" +
    "    document.location.href=f\"https://{rest}\"\n\n" +
    "Menu=menu.Menu\n\n" +
    "trans_menu={\n" +
    "\"menu_console\":{\"en\":\"Console\",\"es\":\"Consola\",\"fr\":\"Console\"},\n" +
    "\"menu_editor\":{\"en\":\"Editor\",\"es\":\"Editor\",\"fr\":\"Editeur\"}\n" +
    "}\n" +
    "links={\n" +
    "\"home\":\"/index.html\",\n" +
    "\"console\":\"/tests/console.html\",\n" +
    "\"editor\":\"/tests/editor.html\"\n" +
    "}\n\n" +
    "languages=[\n" +
    "[\"en\",\"English\"],\n" +
    "[\"fr\",\"Fran\u00e7ais\"]\n" +
    "]\n\n" +
    "doc_versions=[\"3.12\",\"3.11\",\"3.10\"]\n\n" +
    "if 'static_doc'in window.location.href:\n\n" +
    "    current_version=window.location.href.split('/')[4]\n\n" +
    "    table=document.select_one(\".main-table\")\n" +
    "    td=table.select_one('tr').select_one('td')\n" +
    "    sel_version=html.SELECT(id=\"version\")\n" +
    "    for doc_version in doc_versions:\n" +
    "        sel_version <=html.OPTION(doc_version,\n" +
    "        selected=doc_version ==current_version)\n" +
    "    td.insertBefore(html.H5(\"Version \"+sel_version),td.firstChild)\n\n" +
    "    @bind(sel_version,'change')\n" +
    "    def change(ev):\n" +
    "        global current_version\n" +
    "        new_version=ev.target.selectedOptions[0].value\n" +
    "        new_href=window.location.href.replace(current_version,new_version)\n" +
    "        current_version=new_version\n" +
    "        window.location.href=new_href\n\n\n" +
    "def show(language=None ):\n" +
    "    has_req=False\n" +
    "    qs_lang=None\n" +
    "    prefix=\"/\"\n\n" +
    "    if language is None :\n" +
    "        qs_lang=document.query.getfirst(\"lang\")\n" +
    "        if qs_lang and qs_lang in [\"en\",\"fr\"]:\n" +
    "            has_req=True\n" +
    "            language=qs_lang\n" +
    "        else :\n" +
    "            lang=__BRYTHON__.language\n" +
    "            lang=lang.split('-')[0]\n" +
    "            if lang in [\"en\",\"fr\"]:\n" +
    "                language=lang\n\n" +
    "    language=language or \"en\"\n\n" +
    "    _banner=document[\"banner_row\"]\n\n" +
    "    loc=window.location.href\n" +
    "    current=None\n" +
    "    for key in [\"home\",\"console\",\"editor\"]:\n" +
    "        if links[key]in loc:\n" +
    "            current=key\n" +
    "            break\n\n" +
    "    def load_page(key):\n" +
    "        def f(e):\n" +
    "            href=links[key].format(language=language)\n" +
    "            window.location.href=href+f\"?lang={language}\"\n" +
    "        return f\n\n" +
    "    menu=Menu(_banner,default_css=False )\n\n" +
    "    menu.add_link(trans_menu[\"menu_console\"][language],\n" +
    "    href=links[\"console\"]+f\"?lang={language}\")\n\n" +
    "    menu.add_link(trans_menu[\"menu_editor\"][language],\n" +
    "    href=links[\"editor\"]+f\"?lang={language}\")\n\n" +
    "    sel_lang=html.DIV(Class=\"sel_lang\")\n\n" +
    "    document.body.insertBefore(sel_lang,_banner.nextElementSibling)\n" +
    "    select=html.SELECT(Class=\"language\")\n" +
    "    sel_lang <=select\n" +
    "    selected_lang=language\n" +
    "    for lang1,lang2 in languages:\n" +
    "        select <=html.OPTION(lang2,value=lang1,\n" +
    "        selected=lang1 ==selected_lang)\n\n" +
    "    @bind(select,\"change\")\n" +
    "    def change_language(ev):\n" +
    "        sel=ev.target\n" +
    "        new_lang=sel.options[sel.selectedIndex].value\n" +
    "        head=f\"{protocol}://{host}\"\n" +
    "        new_href=href\n" +
    "        if addr.startswith(\"index.html\")or addr ==\"\":\n" +
    "            new_href=f\"{head}/index.html?lang={new_lang}\"\n" +
    "        elif addr.startswith((\"tests/console.html\",\"tests/editor.html\")):\n" +
    "            elts=addr.split(\"?\")\n" +
    "            new_href=f\"{head}/{elts[0]}?lang={new_lang}\"\n" +
    "        document.location.href=new_href\n\n" +
    "    return qs_lang,language\n", 
    ["browser", "browser.widgets.menu", "sys"] 
]};

__BRYTHON__.update_VFS(scripts);
