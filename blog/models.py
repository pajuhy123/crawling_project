#blog/model.py
from django.db import models
############################

class CrawlingData(models.Model):
    instiz = models.CharField(max_length=200, blank=True)
    link_instiz = models.URLField( blank=True)
    clien = models.CharField(max_length=200, blank=True)
    link_clien = models.URLField( blank=True)
    fmkorea = models.CharField(max_length=200, blank=True)
    link_fmkorea = models.URLField( blank=True)
    ou = models.CharField(max_length=200, blank=True)
    link_ou = models.URLField( blank=True)
    pan = models.CharField(max_length=200, blank=True)
    link_pan = models.URLField( blank=True)
    slr = models.CharField(max_length=200, blank=True)
    link_slr = models.URLField( blank=True)
    mlb = models.CharField(max_length=200, blank=True)
    link_mlb = models.URLField( blank=True)
    inben = models.CharField(max_length=200, blank=True)
    link_inben = models.URLField( blank=True)
    ruri = models.CharField(max_length=200, blank=True)
    link_ruri = models.URLField( blank=True)
    utde = models.CharField(max_length=200, blank=True)
    link_utde = models.URLField( blank=True)
    bobe = models.CharField(max_length=200, blank=True)
    link_bobe = models.URLField( blank=True)
    ygosu = models.CharField(max_length=200, blank=True)
    link_ygosu = models.URLField( blank=True)
    drip = models.CharField(max_length=200, blank=True)
    link_drip = models.URLField( blank=True)
    theqoo = models.CharField(max_length=200, blank=True)
    link_theqoo = models.URLField( blank=True)
    dogge = models.CharField(max_length=200, blank=True)
    link_dogge = models.URLField( blank=True)
    namsung = models.CharField(max_length=200, blank=True)
    link_namsung = models.URLField( blank=True)
    flash1 = models.CharField(max_length=200, blank=True)
    link_flash1 = models.URLField( blank=True)
    flash2 = models.CharField(max_length=200, blank=True)
    link_flash2 = models.URLField( blank=True)
    dream1 = models.CharField(max_length=200, blank=True)
    link_dream1 = models.URLField( blank=True)
    dream2 = models.CharField(max_length=200, blank=True)
    link_dream2 = models.URLField( blank=True)
    bobe2 = models.CharField(max_length=200, blank=True)
    link_bobe2 = models.URLField( blank=True)
    fomos1 = models.CharField(max_length=200, blank=True)
    link_fomos1 = models.URLField( blank=True)
    fomos2 = models.CharField(max_length=200, blank=True)
    link_fomos2 = models.URLField( blank=True)
    ilbe = models.CharField(max_length=200, blank=True)
    link_ilbe = models.URLField( blank=True)

    def __str__(self):
        return self.instiz






