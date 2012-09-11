from amministrazione.models import *
from django.contrib import admin
#from django import forms


admin.site.register(Depositari)
admin.site.register(fatturazione)
admin.site.register(albax)
admin.site.register(autogruquinzanese)
admin.site.register(autooldrati)
admin.site.register(azzurra)
admin.site.register(barbieri)
admin.site.register(belotti)
admin.site.register(beneggi)
admin.site.register(bergamaschi)
admin.site.register(bertoni)
admin.site.register(boschetti)
admin.site.register(brichetti)
admin.site.register(cappelletti)
admin.site.register(carissimi)
admin.site.register(carra)
admin.site.register(carrara)
admin.site.register(catenacci)
admin.site.register(chiari)
admin.site.register(dolci)
admin.site.register(emd)
admin.site.register(esseauto)
admin.site.register(fantoni)
admin.site.register(fbgroup)
admin.site.register(festa)
admin.site.register(foletti)
admin.site.register(fornaci)
admin.site.register(fornoni)
admin.site.register(frassine)
admin.site.register(futura)
admin.site.register(galli)
admin.site.register(gelmini)
admin.site.register(ghislanzoni)
admin.site.register(giavazzi)
admin.site.register(greencar)
admin.site.register(intercar)
admin.site.register(lazzari)
admin.site.register(lazzaroni)
admin.site.register(locatelli)
admin.site.register(maggi)
admin.site.register(masserdotti)
admin.site.register(massolini)
admin.site.register(morandi)
admin.site.register(neri)
admin.site.register(nicoletti)
admin.site.register(nordauto)
admin.site.register(nuovaoberdan)
admin.site.register(officinelozza)
admin.site.register(offredi)
admin.site.register(pedersoli)
admin.site.register(riganti)
admin.site.register(rossi)
admin.site.register(rota)
admin.site.register(scandella)
admin.site.register(scaramuzza)
admin.site.register(soardi)
admin.site.register(stanga)
admin.site.register(stella)
admin.site.register(valcavallina)
#admin.site.register(fattura_proforma)
#admin.site.register(fattura_definitiva)



class DepositariAmministrazione(admin.ModelAdmin):
    list_display = ('Codice', 'Regione_Sociale')
    search_fields = ['depositari']
    
class FatturazioneAmministratione(admin.ModelAdmin):
    list_display = ('numero_targa', 'depositaria')

class AlbaxAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa', 'motivo_ingresso')    

class AutogruquinzaneseAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class AutooldratiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')

class AzzurraAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class BarbieriAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class BelottiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class BeneggiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class BergamaschiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class BertoniAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class BoschettiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class BrichettiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class CappellettiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class CarissimiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class CarraAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class CarraraAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class CatenacciAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class ChiariAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class DolciAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class EmdAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    
    
class EsseautoAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')

class FantoniAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class FbgroupAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class FestaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class FolettiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class FornoniAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class FrassineAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class FuturaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class GalliAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class GelminiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class GhislanzoniAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class GiavazziAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class GreencarAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class IntercarAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class LazzariAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class LazzaroniAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class LocatelliAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class MaggiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class MasserdottiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class MassoliniAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class MorandiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class NeriAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class NicolettiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class NordautoAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class NuovaoberdanAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class OfficinelozzaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class OffrediAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class PedersoliAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class RigantiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class RossiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class RotaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class ScandellaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class ScaramuzzaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class SoardiAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class StangaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class StellaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')    

class ValcavallinaAmministrazione(admin.ModelAdmin):
    list_display = ('numero_targa')   

#class ProformaAmministrazione(forms.ModelForm):
    #list_display = ('fattura_proforma')

#class FatturaAmministrazione(forms.ModelForm):
    #list_display = ('fattura_definitiva') 
