import numpy as np
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3)
arcmin2kpc=cosmo.kpc_proper_per_arcmin(z=0.396)    # in units of kpc/arcmin
arcsec2kpc=cosmo.kpc_proper_per_arcmin(z=0.396)/60. # in units of kpc/arcsec
print arcsec2kpc.value

