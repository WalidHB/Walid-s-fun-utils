from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()


# chrome_options.add_argument("--headless")
chrome_options.add_argument('--ignore-certificate-errors')
chrome_options.add_argument('--ignore-ssl-errors')
chrome_options.add_argument("--log-level=OFF")

browser = webdriver.Chrome(options=chrome_options)


one = 0
two = 1
three = 2

browser.get('http://www.workwithcolor.com/red-color-hue-range-01.htm')
colordb=[]

while True:
    rgb = browser.find_elements_by_class_name("rgb-td")
    name = browser.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div[2]/div[1]/h1').text
    #print(name)
    base = []
    for element in rgb:
        if element.text == 'Red' or element.text == 'Green' or element.text == 'Blue':
            continue
        #print(element.text)
        base.append(int(element.text))


    x = one
    y = two
    z = three
    colordb=[]
    for i in base:
        if x > len(base) - 1:
            break
        point =(base[x], base[y], base[z])
        colordb.append(point)
        x = x + 3
        y = y + 3
        z = z + 3
    print(name + ' = ' + str(colordb))

    if name == 'Pink-Red':
        print('done')
        browser.close()
        print(colordb)
        break
    browser.find_element_by_xpath('/html/body/div[3]/div[5]/div[2]/div/div[2]/p[3]/a').click()


