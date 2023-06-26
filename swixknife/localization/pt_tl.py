

__all__ = ('SezimalLocalePT_TL',)


from .pt_pt import SezimalLocalePT_PT


class SezimalLocalePT_TL(SezimalLocalePT_PT):
    LANG = 'pt'
    LANGUAGE = 'português timorense'

    DEFAULT_TIME_ZONE = 'Asia/Dili'
    DEFAULT_HEMISPHERE = 'S'  # Use 'S' for Southern or 'N' for Northern
