import App from './App.svelte';

let extraData;

const component = document.getElementById("svelte").getAttribute("data-component");
const title = document.getElementById("svelte").getAttribute("data-title");
if (document.getElementById('data') !== null) {	
	extraData = JSON.parse(document.getElementById('data').innerHTML);
}
else {
	extraData = null;
}

const app = new App({
	target: document.getElementById("document-body"),
	props: {
		component: component,
		title: title,
		extraData: extraData
	}
});

export default app;