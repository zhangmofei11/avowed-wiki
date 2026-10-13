import os

ad_head = '''<script async="async" data-cfasync="false" src="https://bauval.org/21/4a36a2e9ecd82db173e2fdc9a458dd82"></script>
<script data-cfasync="false" src="https://bauval.org/14/1595e2e4a322ebb60caf66390fc5a28f"></script>
<script>
  atOptions = {
    'key' : '3d96b9b4465555b174309467bc5c50e5',
    'format' : 'iframe',
    'height' : 250,
    'width' : 300,
    'params' : {}
  };
</script>
<script src="https://bauval.org/22/3d96b9b4465555b174309467bc5c50e5"></script>'''

ad_body = '''<div style="display: flex; justify-content: center; margin: 20px 0;">
    <div id="container-4a36a2e9ecd82db173e2fdc9a458dd82"></div>
</div>'''

files = ['index.html', 'classes.html', 'builds.html', 'quests.html', 'tips.html']

for f in files:
    if not os.path.exists(f):
        print(f'Skipping: {f}')
        continue
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()

    if '3d96b9b4465555b174309467bc5c50e5' not in content:
        content = content.replace('</head>', ad_head + '\n</head>')
        print(f'Added head scripts: {f}')

    if 'container-4a36a2e9ecd82db173e2fdc9a458dd82' not in content:
        content = content.replace('<footer', ad_body + '\n\n<footer')
        print(f'Added container div: {f}')

    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f'Updated: {f}')
