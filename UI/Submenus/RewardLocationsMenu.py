from Class import settingkey
from Class.seedSettings import SeedSettings
from UI.Submenus.SubMenu import KH2Submenu


class RewardLocationsMenu(KH2Submenu):

    def __init__(self, settings: SeedSettings):
        super().__init__(title='Locations', settings=settings, in_layout='horizontal')

        self.start_column()
        self.start_group()
        self.add_option(settingkey.SORA_LEVELS)
        self.add_option(settingkey.SPLIT_LEVELS)
        self.add_option(settingkey.CRITICAL_BONUS_REWARDS)
        self.add_option(settingkey.GARDEN_OF_ASSEMBLAGE_REWARDS)
        self.end_group()

        self.start_group()
        self.add_option(settingkey.REMOVE_POPUPS)
        self.end_group()
        self.end_column()

        self.start_column()
        self.start_group()
        self.add_multiselect_buttons(settingkey.WORLDS_WITH_REWARDS, columns=2, group_title='Worlds',tristate=True)
        self.end_group('Worlds')
        self.end_column()

        self.start_column()
        self.start_group()
        self.add_multiselect_buttons(settingkey.SUPERBOSSES_WITH_REWARDS, columns=1, group_title="Superbosses")
        self.end_group('Superbosses')

        self.start_group()
        self.add_multiselect_buttons(settingkey.MISC_LOCATIONS_WITH_REWARDS, columns=1, group_title='Misc Locations')
        self.end_group('Misc Locations')
        self.end_column()

        settings.observe(settingkey.SORA_LEVELS, self.world_update)

        self.finalizeMenu()
        
    def world_update(self):
        level_setting = self.settings.get(settingkey.SORA_LEVELS)
        _, widget = self.widgets_and_settings_by_name[settingkey.SPLIT_LEVELS]
        if "Level"==level_setting:
            widget.setChecked(False)
            widget.setEnabled(False)
        else:
            widget.setEnabled(True)
