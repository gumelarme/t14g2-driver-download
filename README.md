# Thinkpad T14 Gen 2 driver download

Downloads all driver from the [support page](https://pcsupport.lenovo.com/us/en/products/laptops-and-netbooks/thinkpad-t-series-laptops/thinkpad-t14-gen-2-type-20xk-20xl/downloads/driver-list/).

The list of drivers are available on `driver-list.json`, 
but in case you need to rescrape it, use the snippets on `get_link_categories.js`.
The page needed javascript to run, so BeautifulSoup on it self wouldn't work, 
and pyppeteer is too much hassle for me.


Here is how I did it: 


```javascript
// 1. Setup empty var
let driver = [];

// 2. click on the category then
driver.push(...putTheSnippetsHere())

// go back, and repeat step #2 for every category you want
```





