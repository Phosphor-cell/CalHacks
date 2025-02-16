import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';

export const load = (async (ev) => {
    const index = Number(ev.params.index);
    // I know this should be a query param; let it slide
    if (isNaN(index)) {
        error(404)
    }

    return {
        index
    };
}) satisfies PageLoad;