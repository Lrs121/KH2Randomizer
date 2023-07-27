import textwrap
from Class import seedSettings,settingkey
from Class.seedSettings import SeedSettings, ExtraConfigurationData
from UI.Submenus.SubMenu import KH2Submenu
from PySide6.QtWidgets import QPushButton
from UI.worker import BossEnemyZipWorker


class BossEnemyMenu(KH2Submenu):

    def __init__(self, settings: SeedSettings):
        super().__init__(title='Boss/Enemy', settings=settings, in_layout='horizontal')

        self.start_column()
        self.start_group()
        for setting in seedSettings.boss_settings:
            self.add_option(setting.name)
        self.end_group('Bosses')
        self.end_column()

        self.start_column()
        self.start_group()
        for setting in seedSettings.enemy_settings:
            self.add_option(setting.name)
        self.end_group('Enemies')
        self.start_group()
        boss_enemy_mod_button_ps2 = QPushButton('Generate Boss/Enemy-Only Mod (PCSX2)')
        boss_enemy_mod_button = QPushButton('Generate Boss/Enemy-Only Mod (PC)')
        boss_enemy_mod_tooltip = textwrap.dedent('''
        Generates an OpenKH mod that ONLY randomizes bosses and enemies. Can be useful if using a seed generated outside of this
        generator (using Archipelago.gg or otherwise).
        ''').strip()
        boss_enemy_mod_button.setToolTip(boss_enemy_mod_tooltip)
        boss_enemy_mod_button.clicked.connect(lambda : self._make_boss_enemy_only_mod("PC"))
        self.pending_group.addWidget(boss_enemy_mod_button)
        boss_enemy_mod_button_ps2.setToolTip(boss_enemy_mod_tooltip)
        boss_enemy_mod_button_ps2.clicked.connect(lambda : self._make_boss_enemy_only_mod("PCSX2"))
        self.pending_group.addWidget(boss_enemy_mod_button_ps2)
        self.end_group('Cosmetics-Only Mod')

        self.end_column()

        self.finalizeMenu()

    def _make_boss_enemy_only_mod(self,platform):
        worker = BossEnemyZipWorker(self, self.settings, platform)
        worker.generate_mod()