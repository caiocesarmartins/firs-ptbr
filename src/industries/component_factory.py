from industry import IndustrySecondary, TileLocationChecks

industry = IndustrySecondary(
    id="component_factory",
    accept_cargos_with_input_ratios=[
        # 5 cargos eh? pretty rare
        # realism calls also for Steel Wire Rod, but it's a step too far eh
        ("STBR", 2),
        ("STTB", 2),
        ("FOCA", 2),
        ("POWR", 2),
    ],
    combined_cargos_boost_prod=True,
    prod_cargo_types_with_output_ratios=[
        ("VPTS", 3),
        ("PUMP", 3),
        ("LFEQ", 2),
    ],
    prob_in_game="1",  # low chance of build during gameplay
    prob_map_gen="8",
    map_colour="166",
    name="string(STR_IND_COMPONENT_FACTORY)",
    nearby_station_name="string(STR_STATION_COMPONENTS)",
    fund_cost_multiplier="95",
    pollution_and_squalor_factor=1,
)

industry.enable_in_economy(
    "STEELTOWN",
)

industry.add_tile(
    id="component_factory_tile_1",
    location_checks=TileLocationChecks(
        require_effectively_flat=True, disallow_industry_adjacent=True
    ),
)

spriteset_ground = industry.add_spriteset(
    type="dirty_concrete",
)
spriteset_ground_overlay = industry.add_spriteset(type="empty")
spriteset_1 = industry.add_spriteset(
    sprites=[(10, 60, 64, 100, -31, -66)],
)
spriteset_2 = industry.add_spriteset(
    sprites=[(80, 60, 64, 100, -31, -66)],
)
spriteset_3 = industry.add_spriteset(
    sprites=[(150, 60, 64, 100, -31, -66)],
)
spriteset_4 = industry.add_spriteset(
    sprites=[(220, 60, 64, 51, -31, -20)],
)
spriteset_5 = industry.add_spriteset(
    sprites=[(290, 60, 64, 51, -31, -20)],
)
spriteset_6 = industry.add_spriteset(
    sprites=[(360, 60, 64, 31, -31, 0)],
)
spriteset_7 = industry.add_spriteset(
    sprites=[(430, 60, 64, 31, -31, 0)],
)

industry.add_spritelayout(
    id="component_factory_spritelayout_large_building_1",
    tile="component_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_1],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="component_factory_spritelayout_large_building_2",
    tile="component_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_2],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="component_factory_spritelayout_large_building_3",
    tile="component_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_3],
    fences=["nw", "ne", "se", "sw"],
)
industry.add_spritelayout(
    id="component_factory_spritelayout_4",
    tile="component_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[spriteset_4],
    fences=["nw", "ne", "se"],
)
industry.add_spritelayout(
    id="component_factory_spritelayout_5",
    tile="component_factory_tile_1",
    ground_sprite=spriteset_ground,
    ground_overlay=spriteset_ground_overlay,
    building_sprites=[
        spriteset_6
    ],  # out of order spriteset number, due to historical crap, can fix by tidying spritesheet
    fences=["nw", "ne", "se", "sw"],
)

industry.add_industry_layout(
    id="component_factory_industry_layout_1",
    layout=[
        (
            0,
            0,
            "component_factory_spritelayout_large_building_2",
        ),
        (
            0,
            1,
            "component_factory_spritelayout_large_building_3",
        ),
        (
            0,
            2,
            "component_factory_spritelayout_large_building_2",
        ),
        (
            0,
            3,
            "component_factory_spritelayout_large_building_3",
        ),
        (
            0,
            4,
            "component_factory_spritelayout_large_building_3",
        ),
        (
            1,
            0,
            "component_factory_spritelayout_large_building_1",
        ),
        (1, 1, "component_factory_spritelayout_4"),
        (1, 2, "component_factory_spritelayout_5"),
        (1, 3, "component_factory_spritelayout_4"),
        (1, 4, "component_factory_spritelayout_4"),
        (
            2,
            0,
            "component_factory_spritelayout_large_building_2",
        ),
        (
            2,
            1,
            "component_factory_spritelayout_large_building_3",
        ),
        (2, 2, "component_factory_spritelayout_5"),
        (2, 3, "component_factory_spritelayout_5"),
        (2, 4, "component_factory_spritelayout_5"),
    ],
)
