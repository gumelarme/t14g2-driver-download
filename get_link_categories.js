$$("div.table-children-row-warpper").map(x => {
    const name = x.querySelector("div.table-body-item");
    const link = x.querySelector("a[href^='https://download']").href;
    const friendlyName = name.innerText.toLowerCase().replaceAll(" ", "-");
    const version = x.querySelector(".table-version").innerText;
    const severity = x.querySelector("span[class^=severity]").innerText.toLowerCase();

    const releaseDate = x.querySelector(".table-body-width-item:has(.table-version) + div").innerText.toLowerCase().replaceAll(" ", "-");

    return {
        name: friendlyName + "_" + link.substring(link.lastIndexOf("/") + 1),
        link,
        version,
        severity,
        releaseDate,
    }
})