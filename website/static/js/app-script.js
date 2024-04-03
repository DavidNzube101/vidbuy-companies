new_company_el = document.querySelector("#new-company")
new_company_trigger = document.querySelector(".new-company-trigger")
new_company_trigger_close = document.querySelector(".new-company-trigger-close")

new_company_trigger.addEventListener('click', ()=>{
	new_company_el.style.display = "grid"
	new_company_trigger_close.style.display = "block"
})
new_company_trigger_close.addEventListener('click', ()=>{
	new_company_el.style.display = 'none'
	new_company_trigger_close.style.display = "none"
})

accountIcon = document.querySelector("#account-profile")
hm_modal = document.querySelector("#hamburger-menu")
hm_modal_close = document.querySelector("#closehamburger-menuBtn")

accountIcon.addEventListener('click', ()=>{
	hm_modal.style.display = "block"
})
hm_modal_close.addEventListener('click', ()=>{
	hm_modal.style.display = "none"
})

user_theme_preference = "{{ CurrentUser['app_theme'] }}"
console.log(`[INFO]: Current theme ${user_theme_preference}`)
function switchMode() {
	document.querySelector(".switch-theme-button").innerHTML = "Switching"
	fetch ("/change-app-theme", {
		method: 'POST',
		body: JSON.stringify({ current_app_theme: user_theme_preference }),
	}).then((_res) => {
		window.location.href = '/dashboard'
	})
}

tba_btn1 = document.querySelector(".TBA-btn1")
tba_btn2 = document.querySelector(".TBA-btn2")
tba_btn3 = document.querySelector(".TBA-btn3")
ld_modal = document.querySelector("#loader-menu")
ld_modal_close = document.querySelector("#closeloader-menuBtn")

function showLoader(){
	ld_modal.style.display = "block"
}
ld_modal_close.addEventListener('click', ()=>{
	ld_modal.style.display = "none"
})
window.addEventListener('reload', ()=>{
	ld_modal.style.display = "block"
})