from selenium import webdriver
import time

driver = webdriver.Firefox()

universities= { 
    "hse": "https://www.coursera.org/search?query=higher%20school%20of%20economics&page=1&configure%5BclickAnalytics%5D=true&indices%5Bprod_all_products_term_optimization%5D%5BrefinementList%5D%5BentityTypeDescription%5D%5B0%5D=Courses&indices%5Bprod_all_products_term_optimization%5D%5BrefinementList%5D%5Bpartners%5D%5B0%5D=National%20Research%20University%20Higher%20School%20of%20Economics&indices%5Bprod_all_products_term_optimization%5D%5Bpage%5D=1&indices%5Bprod_all_products_term_optimization%5D%5Bconfigure%5D%5BclickAnalytics%5D=true&indices%5Bprod_all_products_term_optimization%5D%5Bconfigure%5D%5BruleContexts%5D%5B0%5D=en&indices%5Bprod_all_products_term_optimization%5D%5Bconfigure%5D%5BhitsPerPage%5D=10"
}


def go_to_url(url):
    driver.get(url)
 

def click_next():
        
    try:
        button = driver.find_element_by_xpath("//button[@id='pagination_right_arrow_button']")
        button.click()
        time.sleep(2)
    
    except Exception:
        print("Error")


def get_all_urls():
    results = driver.find_elements_by_xpath("//li[@class='ais-InfiniteHits-item']//a")
    hrefs = [result.get_attribute("href") for result in results if "/learn/" in result.get_attribute("href")]
    print(f"{len(hrefs)} course links were found")
    time.sleep(2)
    return hrefs


def main():
    try:
        url = universities["hse"]
        go_to_url(url)
        time.sleep(2)
        pages = int(driver.find_elements_by_css_selector('#pagination_number_box_button')[-1].get_attribute("innerHTML").splitlines()[0])
        page = 1
        while page <= pages:
            time.sleep(2)
            links = get_all_urls()
            with open("hse_courses.csv", "a") as file:
                for link in links:
                    file.write(link + "\n")
            print(f"Written {len(links)} lines")
            time.sleep(2)
            click_next()
            page += 1

        driver.close()

    except Exception as e:
        print(e)
        driver.close()

if __name__ == '__main__':
    main()
