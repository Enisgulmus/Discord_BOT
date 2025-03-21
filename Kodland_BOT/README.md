#  Discord Görev Yönetim Botu

Bu proje, küçük ekiplerin görevlerini kolayca yönetebilmesi için oluşturulmuş bir Discord botudur. Bot, görev ekleme, silme, tamamlama ve listeleme gibi temel işlevleri destekler. Tüm veriler kalıcı olarak bir SQLite veritabanında saklanır ve bot yeniden başlatıldığında bile kaybolmaz.

---
##  Özellikler

-  Görev ekleme
-  Görev silme
-  Görevleri listeleme (sıralı gösterim)
-  Görevi tamamlanmış olarak işaretleme
-  SQLite ile veritabanı
-  `pytest` ile birim test desteği

---
##  Kurulum

### Gerekli Kütüphaneleri Yükle

```bash
pip install -r requirements.txt

