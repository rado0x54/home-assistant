"""Offer device oriented automation."""
import voluptuous as vol

from homeassistant.const import CONF_DOMAIN, CONF_PLATFORM
from homeassistant.loader import async_get_integration


# mypy: allow-untyped-defs, no-check-untyped-defs

TRIGGER_SCHEMA = vol.Schema(
    {vol.Required(CONF_PLATFORM): "device", vol.Required(CONF_DOMAIN): str},
    extra=vol.ALLOW_EXTRA,
)


async def async_attach_trigger(hass, config, action, automation_info):
    """Listen for trigger."""
    integration = await async_get_integration(hass, config[CONF_DOMAIN])
    platform = integration.get_platform("device_trigger")
    return await platform.async_attach_trigger(hass, config, action, automation_info)
