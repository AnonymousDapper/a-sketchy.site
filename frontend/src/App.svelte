<script>
	// When adding a new component, it must be imported in this section.
	import Test from './Test.svelte';

	export let component;
	export let title;
	export let extraData;
	
	// Give component a name to match what is passed in from Flask backend
	let components = {
		"test": Test,
	}
</script>

<main>
<svelte:component this={components[component]} {title} {extraData} />
</main>