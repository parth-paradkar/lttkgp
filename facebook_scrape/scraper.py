from selenium.webdriver import Firefox
import time

def scrape():
    d = Firefox()
    d.get("https://facebook.com/groups/lttkgp")
    time.sleep(3)
    h = d.find_elements_by_xpath("//div[@role='article']")

    all_values = []

    for y in h:
        ans = {}

        try:
            assert y.text.find(" shared") != -1
            ans['user'] = y.text.split(" shared")[0]
        
            link = [p.get_attribute('href') for p in y.find_elements_by_tag_name("a") if "youtu" in p.get_attribute('href')][0]
            link = link.split("&")[0].replace("https://l.facebook.com/l.php?u=https%3A%2F%2F", "").replace("%2F", "/").replace("%3A", ":").replace("%3F", "?").replace("%3D", "=").split("https://")[0]
            ans['link'] = link

            upstr = y.text.split("\nLike")[0]
            up = ""
            for c in upstr[::-1]:
                if '0' <= c <= '9':
                    up = c + up
                else:
                    break
            up = int(up)
            ans['up'] = up
        except:
            ans['up'] = 0
        print(ans) 
        all_values.append(ans)

    d.close()


if __name__ == '__main__':
    scrape()
