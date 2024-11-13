class KelasOlahraga:
    def __init__(self, jenis_olahraga, jumlah_peserta):
        self.__jenis_olahraga = jenis_olahraga
        self._jumlah_peserta = jumlah_peserta
        
    def tampilkan_info(self):
        print(f"Jenis Olahraga: {self.__jenis_olahraga}")
        print(f"Jumlah Peserta: {self._jumlah_peserta}")

class KelasTurunanOlahraga(KelasOlahraga):
    def akses_jumlah_peserta(self):
        print(f"Mengakses Jumlah Peserta: {self._jumlah_peserta}")



obj_olahraga = KelasOlahraga("Basket", 15)
obj_olahraga.tampilkan_info()

obj_turunan_olahraga = KelasTurunanOlahraga("Futsal", 10)
obj_turunan_olahraga.akses_jumlah_peserta()