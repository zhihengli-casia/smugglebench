# Release Checklist

- Confirm whether the source images can be redistributed, or keep the release annotation-only.
- If the public SmuggleBench release only includes 1,700 violating samples, remove any leftover `annotations/**/negative/` files before publishing.
- Add the paper title, author list, and citation once the manuscript is public.
- Replace any placeholder model examples in `README.md` with the exact baselines you want to advertise.
- Run a final manual review on `annotations/` to confirm no private filesystem paths remain.
- If you plan to release model outputs, publish only cleaned benchmark results rather than raw internal logs.
