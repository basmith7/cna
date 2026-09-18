Subject: Sandtable — would an open restated-rules repo with stable case IDs be useful to you?

Hi Dylan,

I found Sandtable while surveying what exists for CNA, and your source-material spike reaches the same conclusions I did independently (1979 + Sept errata as authority, interpretations recorded explicitly, no SPI assets in the repo). Nice work — it's clearly the most serious engine effort out there.

I'm not building a competing engine right now. I'm building the thing upstream of one: an openly licensed, restated edition of the Land Game rules plus the common tables as JSON with schemas, with SPI case numbers preserved as citation anchors and a reviewed rulings log (seeded from NJHarman's CC-BY-SA house rules). Your docs cite rules as CNA1979:8.22 and say "source references must not embed copied rules prose" — this would be a public, versioned target for exactly those references, and the JSON tables could replace hand-transcribed fixtures.

Questions:

- Would that be useful to you? If so, what shape would make it drop-in — ID grammar, JSON layout, anything from your content-pack schema I should align with?
- Is there anything you've already resolved (rulings, table transcriptions) that you'd be willing to see upstreamed, with attribution?
- Sandtable has no licence file yet. Not my business, but if you ever want it to outlive one maintainer, it'd matter.

Repo: github.com/basmith7/cna (going public shortly). Design doc on request.

Brian
