from ._compat import fix_line_endings


class TipFormatter(object):
    def render(self, tip):
        raise NotImplementedError


class PlainTipFormatter(TipFormatter):
    def render(self, tip):
        print(fix_line_endings(tip.tipstr))


class BoxTipFormatter(TipFormatter):
    def __init__(self, top="-", bottom="-", left="|", right="|", corner="+"):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right
        self.corner = corner

    def render(self, tip):
        lines = tip.tipstr.split("\n")
        lines.append("")
        lines.insert(0, "")
        lines.insert(0, "TIP #{}".format(tip.tipid))
        width = max(len(l) for l in lines)

        print("{}{}{}".format(self.corner, self.top * (width + 2), self.corner))
        for l in lines:
            print("{} {} {}".format(self.left, l.ljust(width), self.right))
        print("{}{}{}".format(self.corner, self.bottom * (width + 2), self.corner))


ALL_FORMATTERS = {"box": BoxTipFormatter, "plain": PlainTipFormatter}
