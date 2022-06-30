# CDS ERA5 Downloader via wrapped atlite.Cutout

from utils import data


data.cutout_download('Germany', 
					'2019-01-01', '2019-12-31',
					'C:/CaT/Masterthesis/repository/data/era5/',
					req = 'M',
					shape_filter = 'C:/CaT/Masterthesis/data/luisa.tif',
					feature = 'wind'
					)



