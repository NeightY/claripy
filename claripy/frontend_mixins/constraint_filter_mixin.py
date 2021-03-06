class ConstraintFilterMixin(object):
    def _constraint_filter(self, constraints, **kwargs):
        if len(constraints) == 0:
            return constraints

        filtered = super(ConstraintFilterMixin, self)._constraint_filter(constraints, **kwargs)
        ccs = [ self._concrete_constraint(c) for c in filtered ]
        if False in ccs:
            raise UnsatError("Constraints contain False.")
        else:
            return tuple((o if n is None else o) for o,n in zip(constraints, ccs) if n is not True)

    def add(self, constraints, **kwargs):
        if len(constraints) == 0:
            return [ ]

        try:
            ec = self._constraint_filter(constraints)
        except UnsatError:
            ec = list(constraints) + [ false ]

        if len(ec) > 0:
            return super(ConstraintFilterMixin, self).add(ec, **kwargs)
        else:
            return [ ]

    def satisfiable(self, extra_constraints=(), **kwargs):
        try:
            ec = self._constraint_filter(extra_constraints)
            return super(ConstraintFilterMixin, self).satisfiable(extra_constraints=ec, **kwargs)
        except UnsatError:
            return False

    def eval(self, e, n, extra_constraints=(), **kwargs):
        ec = self._constraint_filter(extra_constraints)
        return super(ConstraintFilterMixin, self).eval(e, n, extra_constraints=ec, **kwargs)

    def batch_eval(self, exprs, n, extra_constraints=(), **kwargs):
        ec = self._constraint_filter(extra_constraints)
        return super(ConstraintFilterMixin, self).batch_eval(exprs, n, extra_constraints=ec, **kwargs)

    def max(self, e, extra_constraints=(), **kwargs):
        ec = self._constraint_filter(extra_constraints)
        return super(ConstraintFilterMixin, self).max(e, extra_constraints=ec, **kwargs)

    def min(self, e, extra_constraints=(), **kwargs):
        ec = self._constraint_filter(extra_constraints)
        return super(ConstraintFilterMixin, self).min(e, extra_constraints=ec, **kwargs)

    def solution(self, e, v, extra_constraints=(), **kwargs):
        ec = self._constraint_filter(extra_constraints)
        return super(ConstraintFilterMixin, self).solution(e, v, extra_constraints=ec, **kwargs)

    def is_true(self, e, extra_constraints=(), **kwargs):
        ec = self._constraint_filter(extra_constraints)
        return super(ConstraintFilterMixin, self).is_true(e, extra_constraints=ec, **kwargs)

    def is_false(self, e, extra_constraints=(), **kwargs):
        ec = self._constraint_filter(extra_constraints)
        return super(ConstraintFilterMixin, self).is_false(e, extra_constraints=ec, **kwargs)

from ..errors import UnsatError
from .. import false
