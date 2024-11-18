from flask import Flask, render_template
from requests_html import HTMLSession

app = Flask(__name__)
@app.route('/')


def main():
  s = HTMLSession()
  query = 'New York'
  url = f'https://www.google.com/search?q=weather+{query}'

  r = s.get(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'})

  temp = r.html.find('span#wob_tm', first=True).text
  unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
  desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

  return render_template('index.html', temp=temp, unit=unit, desc=desc)

if __name__ == '__main__':
  app.debug = True
  app.run()