from django.db import models
#from django.core.files.storage import FileSystemStorage
#from django.core.files.storage import FileSystemStorage, default_storage, Storage
#from django.core.files.base import ContentFile
#from django.conf import settings
#from django.shortcuts import rcodiceonse
#from django.http import HttpResponseRedirect
#from django import forms
#fs = default_storage.save('media/photos', ContentFile('new content'))
#fpdf = default_storage.save('media/pdf', ContentFile('new content'))
 
# Create your models here.
#class DepositariAdmin (admin.ModelAdmin):
    #list_display = ('depositari', 'Codice')
#fs = FileSystemStorage(base_url='/photos/custodia')

#class Depositari (models.Model):
class Depositari (models.Model):
    #list_display = ('Depositari', 'Codice')
    Codice = models.CharField(max_length=10)
    Regione_Sociale = models.CharField(max_length=100)
    Categoria = models.CharField(max_length=20)
    Telefono = models.IntegerField(blank=True)
    Fax = models.IntegerField(blank=True)
    Indirizzo = models.CharField(max_length=100, blank=True)
    Localita = models.CharField(max_length=50, blank=True )
    Provincia = models.CharField(max_length=2, blank=True)
    Partita_Iva = models.IntegerField(blank=True)
    Codice_Fiscale = models.CharField(max_length=20, blank=True)
    Email = models.EmailField(max_length=75, blank=True)
    Coordinate_Google_Maps = models.CharField(max_length=30, blank=True)
    def __unicode__(self):
        return u"%s" % (self.Regione_Sociale)
    class Meta:
        verbose_name_plural = "Depositari"

class fatturazione (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    #inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    #immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    #immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    #immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    #immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    #immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    #file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    #file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.depositario)
    class Meta:
        verbose_name_plural = "Dati Custodia"
    
    
#class MyStorage(Storage):
    #def __init__ (self, option=None):
        #option = settings.CUSTOM_STORAGE_OPTIONS
        
    #class Meta:
        #verbose_name_plural = "File"
        
        
        
        
        
class albax (models.Model):
    #custodia = models.ForeignKey('custodia')
    numero_targa = models.CharField(max_length=10)
    #numero_targa = models.ForeignKey('numero_targa')
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    #def save (self, *args, **kwargs):
        #if self.motivo_ingresso == "sequestro":
            #return self.durata_in_giorni_del_fermo == "indeterminato"
        #else:
            #super(albax, self).save(*args, **kwargs)

#class MyStorage(Storage):
    #def __init__ (self, option=None):
        #option = settings.CUSTOM_STORAGE_OPTIONS

    #inserire_documenti_in_pdf_1 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000)
    #inserire_documenti_in_pdf_2 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000, blank=True)
    #inserire_documenti_in_pdf_3 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000, blank=True)
    #inserire_documenti_in_pdf_4 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000, blank=True)
    #inserire_documenti_in_pdf_5 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000, blank=True)
    #immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    #immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    #immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    #immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    #immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    
    immagine_1 = models.FileField (upload_to = "/photos/custodia/", max_length=1000)
    immagine_2 = models.FileField (upload_to = "/photos/custodia/", max_length=1000)
    immagine_3 = models.FileField (upload_to = "/photos/custodia/", max_length=1000)
    immagine_4 = models.FileField (upload_to = "/photos/custodia/", max_length=1000)
    immagine_5 = models.FileField (upload_to = "/photos/custodia/", max_length=1000)
    #immagine_1 = models.FileField(upload_to=fs, max_length=1000)
    #immagine_2 = models.FileField(upload_to=fs, max_length=1000)
    #immagine_3 = models.FileField(upload_to=fs, max_length=1000) 
    #immagine_4 = models.FileField(upload_to=fs, max_length=1000)
    #immagine_5 = models.FileField(upload_to=fs, max_length=1000)


    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)

    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/proforma/", max_length=20000, blank=True)
    #default_storage.open(fpdf).read()
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/finale/", max_length=20000,  blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s %s" %(self.numero_targa, self.tipo_veicolo)
    #def get_valid_name(self):
        #return "/media/photos/%s" % self.id
    #def get_absolute_url(self):
        #url = u'/media/photos/%s'
    #def upload_file(request):
        #if request.method == 'POST':
	    #form = UploadFileForm (request.POST, request.FILES)
	    #if form.is_valid():
	        #handle_uploaded_file(request.FILES['file'])
	        #return HttpResponseRedirect('/media/photos/')
    class Meta:
        verbose_name_plural = "Dati Custodia - Albax"


class autogruquinzanese (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    #inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    #file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    #file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Autogruquinzanese"


class autooldrati (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
    #    (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    #inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)  

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    #file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    #file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s %s" %(self.numero_targa, self.tipo_veicolo)
    class Meta:
        verbose_name_plural = "Dati Custodia - Auto Oldrati"




class azzurra (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Azzurra"


class barbieri (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Barbieri"


class belotti (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=1000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=1000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Belotti"


class beneggi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Beneggi"


class bergamaschi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Bergamaschi"


class bertoni (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    #inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Bertoni"


class boschetti (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    #inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Boschetti"


class brichetti (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Brichetti"


class cappelletti (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Cappelletti"


class carissimi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Carissimi"


class carra (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Carra"


class carrara (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Carrara"


class catenacci (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Catenacci"


class chiari (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Chiari"


class dolci (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Dolci"
        
        
class emd (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Emd"


class esseauto (models.Model):
    #custodia = models.ForeignKey('custodia')
    numero_targa = models.CharField(max_length=10)
    #numero_targa = models.ForeignKey('numero_targa')
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    #def save (self, *args, **kwargs):
        #if self.motivo_ingresso == "sequestro":
            #return self.durata_in_giorni_del_fermo == "indeterminato"
        #else:
            #super(albax, self).save(*args, **kwargs)

#class MyStorage(Storage):
    #def __init__ (self, option=None):
        #option = settings.CUSTOM_STORAGE_OPTIONS

    #inserire_documenti_in_pdf_1 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000)
    #inserire_documenti_in_pdf_2 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000, blank=True)
    #inserire_documenti_in_pdf_3 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000, blank=True)
    #inserire_documenti_in_pdf_4 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000, blank=True)
    #inserire_documenti_in_pdf_5 = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/fpdf", max_length=1000, blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)



    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #default_storage.open(fpdf).read()
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000,  blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s %s" %(self.numero_targa, self.tipo_veicolo)
    #def get_valid_name(self):
        #return "/media/photos/%s" % self.id
    #def get_absolute_url(self):
        #url = u'/media/photos/%s'
    #def upload_file(request):
        #if request.method == 'POST':
	    #form = UploadFileForm (request.POST, request.FILES)
	    #if form.is_valid():
	        #handle_uploaded_file(request.FILES['file'])
	        #return HttpResponseRedirect('/media/photos/')
    class Meta:
        verbose_name_plural = "Dati Custodia - Esseauto"



class fantoni (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Fantoni"


class fbgroup (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Fbgroup"


class festa (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Festa"


class foletti (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Foletti"


class fornaci (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Fornaci"


class fornoni (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Fornoni"


class frassine (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Frassine"


class futura (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Futura"


class galli (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Galli"


class gelmini (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Gelmini"


class ghislanzoni (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Ghislanzoni"


class giavazzi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Giavazzi"


class greencar (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Greencar"


class intercar (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Intercar"


class lazzari (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Lazzari"


class lazzaroni (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Lazzaroni"


class locatelli (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Locatelli"


class maggi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Maggi"


class masserdotti (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Masserdotti"


class massolini (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Massolini"


class morandi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Morandi"


class neri (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Neri"


class nicoletti (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Nicoletti"


class nordauto (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Nordauto"
        

class nuovaoberdan (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Nuovaoberdan"


class officinelozza (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Officine Lozza"


class offredi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Offredi"

class pedersoli (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Pedersoli"
        
        
class riganti (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Riganti"

class rossi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Rossi"


class rota (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Rota"


class scandella (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Scandella"


class scaramuzza (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Scaramuzza"


class soardi (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Soardi"


class stanga (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Stanga"


class stella (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Stella"


class valcavallina (models.Model):
    numero_targa = models.CharField(max_length=10)
    numero_telaio = models.CharField(max_length=30, blank=True)

    TIPO_VEICOLO = (
        (u'altro autoveicolo', u'altro autoveicolo'),
        (u'altro motoveicolo', u'altro motoveicolo'),
        (u'autobus', u'autobus'),
        (u'autocarro', u'autocarro'),
        (u'autovettura', u'autovettura'),
        (u'camper', u'camper'),
        (u'ciclomotore', u'ciclomotore'),
        (u'macchine agricole', u'macchine agricole'),
        (u'moticiclo', u'moticiclo'),
        (u'rimorchio', u'rimorchio'),
        (u'roulotte', u'roulotte'),
        (u'trattore stradale', u'trattore stradale'),
        (u'veicolo non riciclabile', u'veicolo non riciclabile'),
        (u'veicolo storico', u'veicolo storico'),
    )
    tipo_veicolo = models.CharField(max_length=30, choices=TIPO_VEICOLO)
    marca_veicolo = models.CharField(max_length=50)
    modello_veicolo = models.CharField(max_length=50)
    specifica_modello = models.CharField(max_length=100, blank=True)
    colore = models.CharField(max_length=10, blank=True)
    descrizione = models.CharField(max_length=200, blank=True)
    
    MASSA = (
        (u'fino a 1.5t', u'fino a 1.5t'),
        (u'superiore a 1.5 e fino a 3.5t', u'superiore a 1.5 e fino a 3.5t'),
        (u'oltre 3.5t', u'oltre 3.5t'),
    )
    massa_Kg = models.CharField(max_length=40, choices=MASSA)
    SCELTA = (
        (u'S', u'Si'),
        (u'N', u'No'),
    )
    paese_di_origine = models.CharField(max_length=2, choices=SCELTA, blank=True)

    paese_prima_immatricolazione = models.CharField(max_length=30, blank=True)
    immatricolazione = models.CharField(max_length=2, choices=SCELTA, blank=True)
    data_prima_immatricolazione = models.DateField(verbose_name = "data prima immatricolazione", max_length= 8, blank=True)
    note = models.CharField(max_length=100, blank=True)

    depositeria = models.CharField(max_length=100)
    km_percorsi = models.CharField(max_length=20)

    TRASPORTO = (
        (u'con barra o caricato', u'con barra o caricato'),
        (u'recupero fuori sede stradale', u'recupero fuori sede stradale'),
        (u'non previsto', u'non previsto'),
        (u'sollevato', u'sollevato'),
    )
    tipo_di_trasporto = models.CharField(max_length=60, choices=TRASPORTO)

    INTERVENTO = (
        (u'diurno', u'diurno'),
        (u'notturno', u'notturno'),
        (u'festivo', u'festivo'),
        (u'non previsto', u'non previsto'),
    )
    intervento = models.CharField(max_length=30, choices=INTERVENTO)
    custodia_temporanea = models.CharField(max_length=2, choices=SCELTA, blank=True)
    latore = models.CharField(max_length=100)
    
    CUSTODIA = (
        (u'area coperta', u'area coperta'),
        (u'area scoperta', u'area scoperta'),
    )
    tipo_custodia = models.CharField(max_length=30, choices=CUSTODIA)
    data_entrata = models.DateField (max_length=8)
    
    MOTIVOINGRESSO = (
        (u'sequestro', u'sequestro'),
        (u'fermo', u'fermo'),
        (u'confisca definitiva', u'confisca definitiva'),
        (u'cambio depositaria', u'cambio depositaria'),
    )
    motivo_ingresso = models.CharField(max_length=50, choices=MOTIVOINGRESSO)
    data_uscita = models.DateField(max_length=8, blank=True)
    
    MOTIVOUSCITA = (
        (u'acquisto', u'acquisto'),
        (u'affidato al proprietario per rottamazione ai sensi art193', u'affidato al proprietario per rottamazione ai sensi art193'),
        (u'annullamento fermo', u'annullamento fermo'),
        (u'cambio depositeria', u'cambio depositeria'),
        (u'ceduto ad ente pubblico', u'ceduto ad ente pubblico'),
        (u'convertito in fermo c/o proprietario', u'convertito in fermo c/o proprietario'),
        (u'dissequestrato', u'dissequestrato'),
        (u'furto/rapina', u'furto/rapina'),
        (u'preso in custodia dal proprietario dopo 30gg(ciclomotore)', u'preso in custodia dal proprietario dopo 30gg (ciclomotore)'),
        (u'preso in custodia dal proprietario nei 10gg', u'preso in custodia dal proprietario nei 10 gg'),
        (u'fine fermo', u'fine fermo'),
        (u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace', u'ripreso dal proprietario a seguito di sospensione del Giudice di Pace'),
        (u'sopraggiunto sequestro penale', u'sopraggiunto sequestro penale'),
    )
    motivo_uscita = models.CharField(max_length=300, choices=MOTIVOUSCITA, blank=True)
    #con_possesso_Ca = models.CharField(max_length=2, choices=SCELTA, blank=True)
    note_custodia=models.CharField(max_length=200, blank=True)

    ingresso_numero_verbale = models.CharField(max_length=20)
    autorita = models.CharField(max_length=30)
    data_verbale = models.DateField(verbose_name="data verbale", max_length=15)
    comune_emanazione_provvedimento = models.CharField(max_length=50)
    PRESENZA = (
        (u'presente', u'presente'),
        (u'distrutta/mancante', u'distrutta/mancante'),
    )
    targa = models.CharField(max_length=20, choices=PRESENZA)
    bruciato = models.CharField(max_length=2, choices=SCELTA)
    DANNI = (
        (u'danneggiata in modo lieve', u'danneggiata in modo lieve'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'idonea', u'idonea'),
        (u'molto danneggiata', u'molto danneggiata'),
    )
    carrozzeria_anteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_posteriore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_superiore = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_destro = models.CharField(max_length=30, choices=DANNI)
    carrozzeria_lato_sinistro = models.CharField(max_length=30, choices=DANNI)

    MOTORE = (
        (u'distrutto/mancante/non funzionante', u'distrutto/mancante/non funzionante'),
        (u'funzionante', u'funzionante'),
        (u'non previsto', u'non previsto'),
    )
    motore = models.CharField(max_length=50, choices=MOTORE)
    km_percorsi_custodia = models.CharField(max_length=10, blank=True)
    numero_pneumatici_nei_limiti_usura = models.CharField(max_length=1)
    numero_pneumatici_oltre_limiti_usura = models.CharField(max_length=1)

    SCORTA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
        (u'non prevista', u'non prevista'),
    )
    ruota_di_scorta = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_anteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_destro = models.CharField(max_length=25, choices=SCORTA)
    faro_posteriore_sinistro = models.CharField(max_length=25, choices=SCORTA)
    batteria = models.CharField(max_length=25, choices=SCORTA)
    SELLERIA = (
        (u'condizioni normali uso', u'condizioni normali uso'),
        (u'danneggiata', u'danneggiata'),
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'molto danneggiata', u'molto danneggiata'), 
        (u'non previsto', u'non previsto'),
    )
    selleria = models.CharField(max_length=50, choices=SELLERIA)
    IDENTITA = (
        (u'non disponibile del certificati di idoneita tecnica', u'non disponibile del certificato di idoneita tecnica'),
        (u'distrutto/mancante', u'distrutto/mancante'),
        (u'non disponibili archivi elettronici DDT e PRA', u'non disponibili archivi elettronici DDT e PRA'),
        (u'presente', u'presente'),
    )
    documento_di_circolazione = models.CharField(max_length=70, choices=IDENTITA)
    PROPRIETA = (
        (u'distrutta/mancante', u'distrutta/mancante'),
        (u'presente', u'presente'),
    )
    documenti_di_proprieta = models.CharField(max_length=25, choices=PROPRIETA, blank=True)
    veicolo_chiuso_o_privo_di_chiavi = models.CharField(max_length=2, choices=SCELTA)
    diff_dal_verbale_seq_o_fermo = models.CharField(max_length=2, choices=SCELTA)
    FERMO = (
        (u'30', u'30'),
        (u'60', u'60'),
        (u'90', u'90'),
        (u'180', u'180'),
        (u'1 mese', u'1 mese'),
        (u'3 mesi', u'3 mesi'),
        (u'indeterminato', u'indeterminato'),
    )
    durata_in_giorni_del_fermo = models.CharField(max_length=20, choices=FERMO, blank=True)
    inserire_documenti_in_pdf = models.FileField (upload_to = "%Y%m%d", blank=True)
    immagine_1 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)    
    immagine_2 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_3 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_4 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)
    immagine_5 = models.ImageField (upload_to = "/home/alessandro/Scrivania/progetto/media/photos/custodia/", max_length=1000)        

    #fattura_proforma = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_proforma_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/proforma", max_length=20000, blank=True)
    #fattura_finale = models.CharField(max_length=2, choices=SCELTA, blank=True)
    file_pdf_fattura_finale_solo_amministrazione = models.FileField (upload_to = "/home/alessandro/Scrivania/progetto/media/definitiva", max_length=20000, blank=True)
#class Persona (models.Model):
    #TAGLIA = (
        #(u'S', u'small'),
        #(u'M', u'medium'),
    #)
    #name = models.CharField(max_length=60)
    #taglia = models.CharField(max_length=2, choices=TAGLIA)
    def __unicode__(self):
        return u"%s" %(self.numero_targa)
    class Meta:
        verbose_name_plural = "Dati Custodia - Valcavallina"
        
        
#class proforma(forms.Form):
    #class Media:
      #js = ("js/tiny_mce/tiny.js",
              #"js/textarea.js"
              #)
    #fattura_proforma = forms.CharField(widget=forms.Textarea)
