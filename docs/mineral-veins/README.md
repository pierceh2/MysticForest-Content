# Mineral vein unlocks

Gold Vein, Silver Vein and Bronze Vein each have a base appearance and a separate future spell or achievement unlock. Keep each landmark hidden until its own requirement is met. Each vein uses its base sprite across all art packs. The permanent keys are `gold_vein`, `silver_vein` and `bronze_vein`. The unlock criteria and whether earning each unlock grants the item or opens it for purchase are still undecided.

Silver Vein and Bronze Vein are staged with `enabled: false`. Their required `tokenPrice` of 4 is the documented landmark placement placeholder. Confirm prices before release. In an app fixture, grant one vein’s requirement at a time and verify the other two stay locked when the active art pack changes.
