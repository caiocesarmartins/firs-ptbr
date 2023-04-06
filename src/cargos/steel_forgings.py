from cargo import Cargo

cargo = Cargo(
    id="steel_forgings",
    type_name="string(STR_CARGO_NAME_STEEL_FORGINGS)",
    unit_name="string(STR_CARGO_NAME_STEEL_FORGINGS)",
    type_abbreviation="string(STR_CID_STEEL_FORGINGS)",
    sprite="NEW_CARGO_SPRITE",
    weight="1.0",
    is_freight="1",
    cargo_classes="bitmask(CC_PIECE_GOODS)",
    cargo_label="FOCA",
    # apart from TOWNGROWTH_PASSENGERS and TOWNGROWTH_MAIL, FIRS does not set any town growth effects; this has the intended effect of disabling food / water requirements for towns in desert and above snowline
    town_growth_effect="TOWNGROWTH_NONE",
    town_growth_multiplier="1.0",
    units_of_cargo="TTD_STR_TONS",
    items_of_cargo="string(STR_CARGO_UNIT_STEEL_FORGINGS)",
    penalty_lowerbound="14",
    single_penalty_length="255",
    capacity_multiplier="1",
    price_factor=147,
    icon_indices=(4, 6),
    sprites_complete=True,
)