# changing the order of items in econmy list breaks savegames, don't do it.
economies = ["FIRS", "BASIC_TEMPERATE", "BASIC_ARCTIC", "BASIC_TROPIC", "MISTAH_KURTZ"]

# stuff for configuring supply boost behaviour (relying on list positions is evil, but I want to get this done).
supply_requirements = {'ENSP': [21, 84, 'PRIMARY'], 'FMSP': [14, 56, 'PRIMARY'], 'import_export': [56, 224, 'PORT']}

# Definition of numeric IDs for industries
industry_numeric_ids = dict(coal_mine = 0x00,
                            lime_kiln = 0x01,
                            metal_fabrication_plant = 0x02,
                            sugar_plantation = 0x03,
                            iron_ore_mine = 0x04,
                            bauxite_mine = 0x05,
                            copper_mine = 0x05, # reuse of this ID, ran out of IDs
                            smithy_forge = 0x06,
                            steel_mill = 0x07,
                            aluminium_plant = 0x08,
                            metal_workshop = 0x09,
                            quarry = 0x0A,
                            forest = 0x0B,
                            sawmill = 0x0C,
                            furniture_factory = 0x0D,
                            paper_mill = 0x0E,
                            oil_wells = 0x0F,
                            oil_rig = 0x10,
                            oil_refinery = 0x11,
                            plastics_plant = 0x12,
                            sugar_refinery = 0x13,
                            dredging_site = 0x14,
                            iron_works = 0x15,
                            glass_works = 0x16,
                            recycling_plant = 0x17,
                            recycling_depot = 0x18,
                            junk_yard = 0x19,
                            arable_farm = 0x1A,
                            sheep_farm = 0x1B,
                            dairy_farm = 0x1C,
                            mixed_farm = 0x1D,
                            fruit_plantation = 0x1E,
                            fishing_harbour = 0x1F,
                            fishing_grounds = 0x20,
                            basic_farm = 0x21,
                            grain_mill = 0x22,
                            brewery = 0x23,
                            dairy = 0x24,
                            stockyard = 0x25,
                            machine_shop = 0x26,
                            port = 0x27,
                            fertiliser_plant = 0x28,
                            lumber_yard = 0x29,
                            textile_mill = 0x2A,
                            cement_plant = 0x2B,
                            clay_pit = 0x2C,
                            nitrate_mine = 0x2C, # reuse of this ID, ran out of IDs
                            brick_works = 0x2D,
                            biorefinery = 0x2E,
                            orchard_piggery = 0x2F,
                            ranch = 0x30,
                            chemical_plant = 0x31,
                            coffee_estate = 0x32,
                            bulk_terminal = 0x33,
                            trading_post = 0x34,
                            rubber_plantation = 0x35,
                            fibre_crop_farm = 0x36,
                            diamond_mine = 0x37,
                            food_processor = 0x38,
                            hardware_store = 0x39,
                            hotel = 0x3A,
                            food_market = 0x3B,
                            petrol_pump = 0x3C,
                            general_store = 0x3D,
                            vehicle_factory = 0x3E,
                            builders_yard = 0x3F)
#3F is last ID to be used (64 industry limit)


# Definition of industry tile numeric IDs
# tiles 0-159 currently vacant
tile_numeric_ids = dict(TILE_ARABLEFARM_1 = 160,
                        TILE_BREWERY_1 = 161,
                        TILE_CEMENTPLANT_1 = 162,
                        TILE_FERTILISERPLANT_1 = 163,
                        TILE_BUILDERSYARD_1 = 164,
                        TILE_BRICKWORKS_1 = 165,
                        TILE_BIOREFINERY_1 = 166,
                        TILE_BASICFARM_1 = 167,
                        TILE_SUGAR_PLANTATION_1 = 168,
                        TILE_PORT_1 = 169,
                        TILE_PORT_2 = 170,
                        TILE_ORCHARD_PIGGERY_1 = 171,
                        TILE_ORCHARD_PIGGERY_2 = 172,
                        TILE_RANCH_1 = 173,
                        TILE_COPPER_ORE_MINE_1 = 174,
                        TILE_DAIRY_2 = 175,
                        TILE_PLASTICSPLANT_1 = 176,
                        TILE_QUARRY_1 = 177,
                        TILE_GLASSWORKS_1 = 178,
                        TILE_STOCKYARD_1 = 179,
                        TILE_DAIRYFARM_1 = 180,
                        TILE_DAIRY_1 = 181,
                        TILE_GRAINMILL_1 = 182,
                        TILE_TEXTILEMILL_1 = 183,
                        TILE_FURNITUREFACTORY_1 = 184,
                        TILE_ALUMINIUMPLANT_1 = 185,
                        TILE_MACHINESHOP_1 = 186,
                        TILE_LUMBERYARD_1 = 187,
                        TILE_METALWORKSHOP_1 = 188,
                        TILE_CLAYPIT_1 = 189,
                        TILE_MIXEDFARM_1 = 190,
                        TILE_LIMEKILN_1 = 191,
                        TILE_SHEEPFARM_1 = 192,
                        TILE_JUNKYARD_1 = 193,
                        food_market_tile_1 = 194,
                        TILE_FISHINGHARBOUR_1 = 195,
                        TILE_FISHINGHARBOUR_2 = 196,
                        TILE_BAUXITEMINE_1 = 197,
                        TILE_DREDGINGSITE_1 = 198,
                        TILE_IRONWORKS_1 = 199,
                        TILE_METALFABRICATIONPLANT_1 = 200,
                        TILE_RECYCLINGPLANT_1 = 201,
                        TILE_RECYCLINGDEPOT_1 = 202,
                        TILE_PETROLPUMP_1 = 203,
                        TILE_FISHINGGROUNDS_1 = 204,
                        TILE_FOREST_1 = 205,
                        TILE_FOREST_2 = 206,
                        TILE_FRUITPLANTATION_1 = 207,
                        TILE_FRUITPLANTATION_2 = 208,
                        TILE_FORGE_1 = 209,
                        TILE_LUMBERYARD_2 = 210,
                        TILE_IRONWORKS_2 = 211,
                        TILE_IRONWORKS_3 = 212,
                        TILE_FIBRE_CROP_FARM_1 = 213,
                        TILE_SUGARREFINERY_1 = 214,
                        TILE_OILWELLS_1 = 215,
                        TILE_OILWELLS_2 = 216,
                        hotel_tile_1 = 217,
                        hardware_store_tile_1 = 218,
                        general_store_tile_1 = 219,
                        TILE_COFFEEPLANTATION_1 = 220,
                        TILE_COFFEEPLANTATION_2 = 221,
                        TILE_BULK_TERMINAL_1 = 222,
                        TILE_BULK_TERMINAL_2 = 223,
                        TILE_GENERIC_CONCRETE = 224,
                        TILE_TRADING_POST_1 = 225,
                        TILE_TRADING_POST_2 = 226,
                        TILE_RUBBER_PLANTATION_1 = 227,
                        TILE_RUBBER_PLANTATION_2 = 228,
                        TILE_FOODPROCESSOR_1 = 229,
                        TILE_NITRATEMINE_1 = 230,
                        TILE_CHEMICALPLANT_1 = 231,
                        TILE_VEHICLE_FACTORY_1 = 232)

chameleon_cache_dir =  'chameleon_cache'

# specify location for intermediate files generated during build (nml, graphics, lang etc)
generated_files_dir =  'generated'

# this is for nml or grfcodec, don't need to use python path module here
graphics_path =  'generated/graphics/'

openttd_climates =  ["CLIMATE_TEMPERATE", "CLIMATE_ARCTIC", "CLIMATE_TROPIC", "CLIMATE_TOYLAND"]
