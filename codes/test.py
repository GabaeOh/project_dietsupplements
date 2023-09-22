from selenium import webdriver
import pandas as pd 
import pymongo as mg
import time

wemake = 'https://front.wemakeprice.com/category/section/3100171'
browser =webdriver.Chrome('C:/Users/02-19/Devleops/chromedriver.exe')
browser.get(wemake)


wemake_list = []
wemake_info_name = ['product_name', 'review_name', 'review_content', 'review_date', 'review_rating']


# 한 페이지에 있는 모든 제품의 리뷰를 갖고 오기 
products_path = '.conts_wrap'
products_number = browser.find_elements_by_css_selector(products_path)
for i in range(len(products_number)): 
    try : 
        # 각각의 click_product 클릭
        products_number = browser.find_elements_by_css_selector(products_path)  # 다시 제품 목록 가져오기
        product = products_number[i]  # i번째 제품 선택
        product.click()
        time.sleep(1)
        
        try : 
            product_name = browser.find_element_by_css_selector('#_infoDescription > div.title_box > h3').text
        except : 
            product_name = str()
        
        #리뷰 클릭 
        review_click = browser.find_element_by_css_selector('#_contents > div.content_main.items > div.dinfo_itemdetail > div.wrap_tab > div > ul > li:nth-child(3)').click()
        time.sleep(2) #term을 주기
        
    except:
        pass
    
    # 한 제품의 모든 리뷰 끌고 오기 
    reviews_list = []

    ##리뷰 페이지네이션
    page_path = browser.find_elements_by_css_selector('.link_page')
    
    if len(page_path) > 0:
    # 페이지네이션 버튼이 있을 때만 클릭
    
        for page_number in range (2, 7) :
            selector = 'div.paging_comm > a:nth-child({})'.format(page_number)

            page_elements = browser.find_element_by_css_selector(selector)
            page_elements.click()

            # 리뷰 한페이지 갖고 오기 
            review_bundle = browser.find_elements_by_css_selector('[data-container="reviewItem"]')

            #리뷰가 있으면 갖고 오기 
            if review_bundle: 
                for review in review_bundle:

                    # 리뷰 정보 
                    try : 
                        review_name = review.find_element_by_css_selector('.name').text
                    except : 
                        review_name = str()
                    try : 
                        review_content = review.find_element_by_css_selector('.post').text
                    except :
                        review_content = str()
                    try : 
                        review_date = review.find_element_by_css_selector('.time').text
                    except : 
                        review_date =str()
                    try : 
                        review_rating = review.find_element_by_css_selector('.grade').text 
                    except :
                        review_rating =str()

                    review_info  = [product_name, review_name, review_content, review_date, review_rating]
                    reviews_list.append(review_info)
                    time.sleep(3)

                wemake_list.extend(reviews_list)
                reviews_list = []

    else  : 
        continue
        
    browser.back()