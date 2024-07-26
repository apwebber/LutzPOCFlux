library(jsonlite)
source("lutz_p_flux.R")

npp = c(-1,0,1,100)
svi = c(-1,0,1,999)
ze = c(0,-1,200,6000)

prd_v = prd(svi)
prr_v = prr(svi)
rld_v = rld(svi)
pratio_val = p.ratio(prd(svi),ze,rld(svi),prr(svi))
flux_val = lutz_p_flux(npp,svi,ze)

df = data.frame(
  npp=npp,
  svi=svi,
  ze=ze,
  prd=prd_v,
  prr=prr_v,
  rld=rld_v,
  pratio=pratio_val,
  flux=flux_val
)

print(df)
write(toJSON(df,digits=10), "test_values.json")
