(function () {
	var path = location.pathname;
	if (/\/index\.html?$/i.test(path)) {
		location.replace(
			path.replace(/\/index\.html?$/i, "/") + location.search + location.hash
		);
	}
})();
