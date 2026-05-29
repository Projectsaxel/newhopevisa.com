(function () {
	"use strict";

	var STORAGE_KEY = "newhope-uscis-memo-2026-05-en-v1";

	if (localStorage.getItem(STORAGE_KEY) === "1") {
		return;
	}

	var overlay = document.createElement("div");
	overlay.className = "nhv-popup-overlay";
	overlay.id = "nhv-uscis-popup";
	overlay.setAttribute("role", "dialog");
	overlay.setAttribute("aria-modal", "true");
	overlay.setAttribute("aria-labelledby", "nhv-uscis-popup-title");
	overlay.innerHTML =
		'<div class="nhv-popup">' +
		'<button type="button" class="nhv-popup__close" aria-label="Close notice">&times;</button>' +
		'<div class="nhv-popup__header">' +
		'<h2 class="nhv-popup__title" id="nhv-uscis-popup-title">USCIS Memorandum — Adjustment of Status</h2>' +
		'<p class="nhv-popup__subtitle">Published on May 22, 2026</p>' +
		"</div>" +
		'<div class="nhv-popup__body">' +
		'<p class="nhv-popup__greeting">Good afternoon,</p>' +
		"<p>We would like to share some important clarifications regarding the memorandum published by USCIS on May 22, 2026, concerning Adjustment of Status cases.</p>" +
		"<p>The memorandum reinforces that, under Section 245 of the INA (Immigration and Nationality Act), Adjustment of Status is considered a discretionary and extraordinary benefit. This means that even when a foreign national meets the basic eligibility requirements, approval of the case is not automatic. The final decision depends on the review and discretion of the immigration officer handling the case.</p>" +
		"<p>According to USCIS, it has always been understood that not all eligible applicants will necessarily have their Adjustment of Status approved. The officer may evaluate the evidence submitted, the applicant\u2019s immigration history, and other relevant factors to determine whether granting the benefit is appropriate and in the best interest of the United States.</p>" +
		"<p>The memorandum also emphasizes that Adjustment of Status was not created to replace the regular consular processing system, but rather to apply only to specific situations provided by law.</p>" +
		"<p>As a result, after the interview and case review, an applicant may either receive approval of the Adjustment of Status or be directed to proceed through consular processing. This does not necessarily mean that the individual will lose the opportunity to obtain lawful status; however, the process may become longer and may involve additional costs.</p>" +
		"<p>In the discretionary review process, USCIS instructs officers to consider the totality of the circumstances of each case, including both positive and negative factors. Some of the factors that may be reviewed include:</p>" +
		"<ul>" +
		"<li>immigration or status violations;</li>" +
		"<li>unauthorized employment;</li>" +
		"<li>fraud or misrepresentation;</li>" +
		"<li>immigration history;</li>" +
		"<li>family ties;</li>" +
		"<li>moral character;</li>" +
		"<li>humanitarian factors and other favorable evidence.</li>" +
		"</ul>" +
		"<p>Although, in theory, these guidelines have always applied to Adjustment of Status cases, we still do not know exactly how this new memorandum will affect cases that are currently pending. However, we understand that case reviews may become more detailed and rigorous moving forward.</p>" +
		"<p>We will continue monitoring USCIS guidance and will keep our clients informed regarding any relevant changes.</p>" +
		'<p class="nhv-popup__signature">Sincerely,<br>New Hope Visa</p>' +
		"</div>" +
		'<div class="nhv-popup__footer">' +
		'<label class="nhv-popup__dismiss-label">' +
		'<input type="checkbox" id="nhv-uscis-popup-hide" />' +
		"Do not show again" +
		"</label>" +
		'<button type="button" class="nhv-popup__btn" id="nhv-uscis-popup-ok">I understand</button>' +
		"</div>" +
		"</div>";

	document.body.appendChild(overlay);

	var closeBtn = overlay.querySelector(".nhv-popup__close");
	var okBtn = overlay.querySelector("#nhv-uscis-popup-ok");
	var hideCheckbox = overlay.querySelector("#nhv-uscis-popup-hide");
	var lastFocus = null;

	function openPopup() {
		lastFocus = document.activeElement;
		overlay.classList.add("is-open");
		document.body.classList.add("nhv-popup-open");
		closeBtn.focus();
	}

	function closePopup() {
		if (hideCheckbox.checked) {
			localStorage.setItem(STORAGE_KEY, "1");
		}
		overlay.classList.remove("is-open");
		document.body.classList.remove("nhv-popup-open");
		if (lastFocus && typeof lastFocus.focus === "function") {
			lastFocus.focus();
		}
	}

	closeBtn.addEventListener("click", closePopup);
	okBtn.addEventListener("click", closePopup);

	overlay.addEventListener("click", function (event) {
		if (event.target === overlay) {
			closePopup();
		}
	});

	document.addEventListener("keydown", function (event) {
		if (!overlay.classList.contains("is-open")) {
			return;
		}
		if (event.key === "Escape") {
			closePopup();
		}
	});

	if (document.readyState === "loading") {
		document.addEventListener("DOMContentLoaded", function () {
			setTimeout(openPopup, 400);
		});
	} else {
		setTimeout(openPopup, 400);
	}
})();
